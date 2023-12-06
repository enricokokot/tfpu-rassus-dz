from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Text, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# SQLite database file URL (change the file path as needed)
DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# SQLAlchemy ORM model for the 'items' table
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(Text)

# Create the 'items' table
Base.metadata.create_all(bind=engine)

# SQLAlchemy SessionLocal for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pre-existing data to be inserted into the database
pre_existing_data = [
    {"name": "Item 1", "description": "Description for Item 1"},
    {"name": "Item 2", "description": "Description for Item 2"},
    # Add more items as needed
]

# Function to initialize the database with pre-existing data
def init_db():
    db = SessionLocal()
    try:
        # Ensure the database and tables are created
        Base.metadata.create_all(bind=engine)

        # Insert pre-existing data into the database
        for item_data in pre_existing_data:
            item = Item(**item_data)
            db.add(item)

        # Commit the changes
        db.commit()

        # Query and print the contents of the items table
        items = db.query(Item).all()
        print("Items in the database:")
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
