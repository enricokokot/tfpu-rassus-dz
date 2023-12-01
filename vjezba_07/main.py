import logging
from datetime import datetime
import os
import httpx
import random
import asyncio
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

logging.basicConfig(filename=f'logs/{datetime.today().strftime('%d-%m-%Y')}_pokemon_api_log.txt',
                    encoding='utf-8',
                    level=logging.CRITICAL,
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if os.stat(f'logs/{datetime.today().strftime('%d-%m-%Y')}_pokemon_api_log.txt').st_size == 0:
    with open(f'logs/{datetime.today().strftime('%d-%m-%Y')}_pokemon_api_log.txt',
              'a',
              encoding='utf-8') as f:
        f.write(f"Log file created {
            datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
async def fetch_many_pokemon(pokemon_number):
    pokemon_ids = [random.randint(1, 150) for _ in range(pokemon_number)]
    tasks = [fetch_one_pokemon(pokemon_id) for pokemon_id in pokemon_ids]
    results = await asyncio.gather(*tasks)
    for idx, result in enumerate(results):
        logging.critical(f"Fetched data for Pokemon #{idx + 1}: ID - #{result["id"]},Name - {result["name"]}, Types - {result["type"]}")
    return results

async def fetch_one_pokemon(pokemon_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        response = response.json()
        the_pokemon = {
            "id": pokemon_id,
            "name": response["name"],
            "type": response["types"][0]["type"]["name"]
        }
        return the_pokemon
    
@app.post("/do")
def do(data: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(fetch_many_pokemon, data)
    return { "message": f"Fetching data for {data} random Pokemon from theAPI and logging. Check the log file ({datetime.today().strftime('%d-%m-%Y')}) later." }
