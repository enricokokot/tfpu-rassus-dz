import asyncio
import aiohttp
import json


# 04
async def fetch_url(url):
    await asyncio.sleep(2)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            print(f"Length of response for {url} is: {len(result)}")


async def main():
    urls = [
        "https://example.com",
        "https://google.com",
        "https://github.com",
        "https://www.index.hr/",
        "https://www.bug.hr/",
        "https://www.netokracija.com/",
        "https://www.youtube.com/",
    ]

    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    await asyncio.gather(*tasks)

# asyncio.run(main())


# 05
async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            result = json.loads(result)
            # print(json.dumps(result, indent=2))
            print(f'{{\n    "userId": {result["userId"]}\n    "id": {
                  result["id"]}\n    "title": {result["title"]}\n    "body": {result["body"]}\n}}')


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]

    tasks = [asyncio.create_task(get_json(url)) for url in urls]
    await asyncio.gather(*tasks)

# asyncio.run(main())
