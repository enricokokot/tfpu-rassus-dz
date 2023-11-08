import asyncio
import aiohttp
import random

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            sleep_interval = random.uniform(1, 5)
            await asyncio.sleep(sleep_interval)
            content = await response.read()
            print(f"URL: {url}, Size: {len(content)} bytes")

async def main():
    urls = ['https://example.com', 'https://google.com', 'https://github.com', 'https://www.python.org']
    tasks = [fetch_url(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
