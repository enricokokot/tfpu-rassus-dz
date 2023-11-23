import httpx
import asyncio
import json

async def fetcher(country_name):
    response = httpx.get(f"http://127.0.0.1:8000/{country_name}")
    response = response.json()
    return response

async def main():
    countries = ["croatia", "greece", "italy"]
    tasks = [fetcher(country) for country in countries]
    results = await asyncio.gather(*tasks)
    print(json.dumps(results, indent=2))
    
asyncio.run(main())