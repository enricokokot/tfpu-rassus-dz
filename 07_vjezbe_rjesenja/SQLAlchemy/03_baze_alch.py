from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List

app = FastAPI()

# SQLAlchemy database engine
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

# SQLAlchemy ORM model for the 'items' table
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)

# Create the 'items' table
Base.metadata.create_all(bind=engine)

# SQLAlchemy SessionLocal for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pydantic model for response
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

class ItemSubmit(BaseModel):
    #id: int
    name: str
    description: str

# Function to initialize the database with pre-existing data
def init_db():
    db = SessionLocal()
    try:
        # Ensure the database and tables are created
        Base.metadata.create_all(bind=engine)

        # Insert pre-existing data into the database during initialization
        pre_existing_data = [
            {"name": "Initial Item 1", "description": "Description for Initial Item 1"},
            {"name": "Initial Item 2", "description": "Description for Initial Item 2"},
            # Add more items as needed
        ]

        for item_data in pre_existing_data:
            item = Item(**item_data)
            db.add(item)

        # Commit the changes
        db.commit()

        # Query and print the contents of the items table after initialization
        items = db.query(Item).all()
        print("Items in the database after initialization:")
        for item in items:
            print(f"ID: {item.id}, Name: {item.name}, Description: {item.description}")

    finally:
        db.close()

# Function to disconnect from the database
def shutdown_db():
    engine.dispose()

# FastAPI event to initialize the database when the application starts
@app.on_event("startup")
async def startup_event():
    init_db()

# FastAPI event to disconnect from the database when the application stops
@app.on_event("shutdown")
async def shutdown_event():
    shutdown_db()

# Read all items from the database and return in JSON format
@app.get("/items/", response_model=List[ItemResponse])
async def read_items():
    db = SessionLocal()
    try:
        items = db.query(Item).all()
        return items
    finally:
        db.close()

# Add items to the database
@app.post("/items/create/")
async def create_item(item: ItemSubmit):
    db = SessionLocal()
    try:
        item_model = Item()
        item_model.name = item.name
        item_model.description = item.description
        
        db.add(item_model)
        db.commit()
        db.refresh(item_model)
        return item
    finally:
        db.close()
