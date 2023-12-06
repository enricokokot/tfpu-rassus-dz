from fastapi import FastAPI, HTTPException
from databases import Database
from typing import List
from pydantic import BaseModel

app = FastAPI()

# SQLite database file URL (change the file path as needed)
DATABASE_URL = "sqlite:///./test.db"

# Database connection instance
database = Database(DATABASE_URL)

# Pre-existing data to be inserted into the database during initialization
pre_existing_data = [
    {"name": "Initial Item 1", "description": "Description for Initial Item 1"},
    {"name": "Initial Item 2", "description": "Description for Initial Item 2"},
    # Add more items as needed
]

# Define Pydantic model for item
class ItemModel(BaseModel):
    id: int
    name: str
    description: str

# Function to initialize the database with pre-existing data
async def init_db():
    await database.connect()
    try:
        # Ensure the database and tables are created
        await database.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
            """
        )

        # Insert pre-existing data into the database during initialization
        for item_data in pre_existing_data:
            await database.execute(
                """
                INSERT INTO items (name, description) VALUES (:name, :description)
                """,
                values=item_data,
            )

        # Query and print the contents of the items table after initialization
        query = "SELECT * FROM items"
        items = await database.fetch_all(query)
        print("Items in the database after initialization:")
        for item in items:
            print(item)

    finally:
        await database.disconnect()

# Function to disconnect from the database
async def shutdown_db():
    await database.disconnect()

# FastAPI event to initialize the database when the application starts
@app.on_event("startup")
async def startup_event():
    await init_db()

# FastAPI event to disconnect from the database when the application stops
@app.on_event("shutdown")
async def shutdown_event():
    await shutdown_db()

# Read all items from the database and return in JSON format
@app.get("/items/", response_model=List[ItemModel])
async def read_items():
    query = "SELECT * FROM items"
    items = await database.fetch_all(query)
    return items

# Add items to the database
@app.post("/items/create/")
async def create_item(name: str, description: str):
    query = "INSERT INTO items (name, description) VALUES (:name, :description)"
    values = {"name": name, "description": description}
    item_id = await database.execute(query=query, values=values)
    return {"item_id": item_id, "name": name, "description": description}
