from fastapi import FastAPI
from databases import Database

app = FastAPI()

# SQLite database file URL (change the file path as needed)
DATABASE_URL = "sqlite:///./test.db"

# Database connection instance
database = Database(DATABASE_URL)


# Function to initialize the database
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
