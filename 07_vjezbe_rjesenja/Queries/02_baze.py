from fastapi import FastAPI
from databases import Database

app = FastAPI()

# SQLite database file URL (change the file path as needed)
DATABASE_URL = "sqlite:///./test.db"

# Database connection instance
database = Database(DATABASE_URL)

# Pre-existing data to be inserted into the database
pre_existing_data = [
    {"name": "Item 1", "description": "Description for Item 1"},
    {"name": "Item 2", "description": "Description for Item 2"},
    # Add more items as needed
]


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

        # Insert pre-existing data into the database
        for item_data in pre_existing_data:
            await database.execute(
                """
                INSERT INTO items (name, description) VALUES (:name, :description)
                """,
                values=item_data,
            )

        # Query and print the contents of the items table
        query = "SELECT * FROM items"
        items = await database.fetch_all(query)
        print("Items in the database:")
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
