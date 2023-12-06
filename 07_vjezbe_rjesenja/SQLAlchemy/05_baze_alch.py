from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import httpx
from fastapi import FastAPI, HTTPException,Path
from sqlalchemy import create_engine, Column, Integer, String, Text, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List

app = FastAPI()

# SQLite database file URL (change the file path as needed)
DATABASE_URL = "sqlite:///./api_data.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# JSONPlaceholder API URL (example)
JSONPLACEHOLDER_API_URL = "https://jsonplaceholder.typicode.com/todos"

# Define Pydantic model for item
class ItemModel(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    title = Column(String)
    completed = Column(Text)

# Create the 'items' table
Base.metadata.create_all(bind=engine)

# SQLAlchemy SessionLocal for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to initialize the database with data from an API
async def init_db_with_api_data():
    db = SessionLocal()
    try:
        # Ensure the database and tables are created
        Base.metadata.create_all(bind=engine)

        # Fetch data from the API
        async with httpx.AsyncClient() as client:
            response = await client.get(JSONPLACEHOLDER_API_URL)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from the API")

        api_data = response.json()

         # Check if data already exists in the database
        if db.query(Item).first():
            print("Data already exists in the database. Skipping API fetch and insert.")
            return
        # Insert API data into the database during initialization
        for item_data in api_data:
            item = Item(**item_data)
            db.add(item)
        # Commit the changes
        db.commit()

        # Query and print the contents of the items table after initialization
        items = db.query(Item).all()
        print("Items in the database after initialization:")
        for item in items:
            print(f"ID: {item.id}, Title: {item.title}, Status: {item.completed}")
        
    finally:
        db.close()

# Function to disconnect from the database
async def shutdown_db():
    engine.dispose()

# FastAPI event to initialize the database with API data when the application starts
@app.on_event("startup")
async def startup_event():
    await init_db_with_api_data()

# FastAPI event to disconnect from the database when the application stops
@app.on_event("shutdown")
async def shutdown_event():
    await shutdown_db()

# Read all items from the database and return in JSON format
@app.get("/api_items/", response_model=List[ItemModel])
async def read_api_items():
    db = SessionLocal()
    try:
        items = db.query(Item).all()
        return items
    finally:
        db.close()
