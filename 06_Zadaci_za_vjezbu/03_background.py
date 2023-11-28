from fastapi import FastAPI, BackgroundTasks, Depends
import httpx
import logging
import random
import asyncio

# Set the logging level for the httpx library to WARNING
logging.getLogger("httpx").setLevel(logging.WARNING)

app = FastAPI()

# Create a lock to synchronize write operations to the log file
log_lock = asyncio.Lock()

logging.basicConfig(filename="pokemon_api_log.txt", level=logging.INFO)

async def fetch_pokemon_data_and_log():
    """
    Background task to fetch data about a random Pokemon from the API and log it.
    """
    # Choose a random Pokémon ID (up to Pokémon #150 for simplicity)
    random_pokemon_id = random.randint(1, 150)

    # Fetch data from the Pokémon API without logging the request details
    url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    # Extract relevant information
    pokemon_name = data["name"]
    pokemon_types = [type_info["type"]["name"] for type_info in data["types"]]

    # Log the information with a lock to synchronize write operations
    async with log_lock:
        log_message = f"Fetched data for Pokemon #{random_pokemon_id}: Name - {pokemon_name}, Types - {', '.join(pokemon_types)}"
        logging.info(log_message)

@app.get("/fetch-pokemon-and-log")
async def fetch_pokemon_and_log(background_tasks: BackgroundTasks):
    """
    Endpoint that triggers a background task to fetch and log data about a random Pokemon.
    """
    background_tasks.add_task(fetch_pokemon_data_and_log)
    return {"message": "Fetching random Pokemon data from the API and logging. Check the log file later."}
