import asyncio
import aiohttp
import json


url = "https://pokeapi.co/"

async def get_pokemon(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + "api/v2/pokemon/" + str(id)) as response:
            result = await response.json()
            final_result = {"id": result["id"], "name": result["name"], "height": result["height"]}
            print(json.dumps(final_result, indent=2))

async def main():
    ids = [1, 5, 10, 15]

    tasks = [get_pokemon(id) for id in ids]
    await asyncio.gather(*tasks)

asyncio.run(main())