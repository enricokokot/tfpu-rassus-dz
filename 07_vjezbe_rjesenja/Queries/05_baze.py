from fastapi import FastAPI, HTTPException
from databases import Database
from typing import List
from pydantic import BaseModel
import httpx

app = FastAPI()

# SQLite database file URL (change the file path as needed)
DATABASE_URL = "sqlite:///./api_data.db"

# Database connection instance
database = Database(DATABASE_URL)

# JSONPlaceholder API URL (example)
JSONPLACEHOLDER_API_URL = "https://jsonplaceholder.typicode.com/todos"

# Define Pydantic model for item
class ItemModel(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool

# Function to initialize the database with data from an API
async def init_db_with_api_data():
    await database.connect()
    try:
        # Ensure the database and tables are created
        await database.execute(
            """
            CREATE TABLE IF NOT EXISTS api_data (
                id INTEGER PRIMARY KEY,
                userId INTEGER,
                title TEXT,
                completed BOOLEAN
            )
            """
        )

        # Fetch data from the API
        async with httpx.AsyncClient() as client:
            response = await client.get(JSONPLACEHOLDER_API_URL)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from the API")

        api_data = response.json()

        # Insert API data into the database during initialization
        for item_data in api_data:
            await database.execute(
                """
                INSERT INTO api_data (userId, title, completed) VALUES (:userId, :title, :completed)
                """,
                values={
                    "userId": item_data["userId"],
                    "title": item_data["title"],
                    "completed": item_data["completed"],
                },
            )

        # Query and print the contents of the api_data table after initialization
        query = "SELECT * FROM api_data"
        items = await database.fetch_all(query)
        print("Items in the database after initializing with API data:")
        for item in items:
            print(item)

    finally:
        await database.disconnect()

# Function to disconnect from the database
async def shutdown_db():
    await database.disconnect()

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
    query = "SELECT * FROM api_data"
    items = await database.fetch_all(query)
    return items
