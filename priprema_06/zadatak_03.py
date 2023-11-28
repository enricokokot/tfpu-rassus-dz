from fastapi import FastAPI, BackgroundTasks
import logging
import httpx
import random

app = FastAPI()

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.basicConfig(filename=f'logs/pokemon_api_log.txt',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    )


def fetch_pokemon_data_and_log(pokemon_number, pokemon_name, pokemon_type):
    global logger
    logging.info(f"Fetched data for Pokemon #{
        pokemon_number}: Name - {pokemon_name}, Types - {pokemon_type}")


@app.get("/fetch-pokemon-and-log")
async def fetch_pokemon_and_log(background_tasks: BackgroundTasks):
    pokemon_id = random.randint(1, 151)
    response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    response = response.json()
    background_tasks.add_task(fetch_pokemon_data_and_log,
                              pokemon_id,
                              response["name"],
                              response["types"][0]["type"]["name"])
    return {
        "id": pokemon_id,
        "name": response["name"],
        "types": response["types"][0]["type"]["name"]
    }
