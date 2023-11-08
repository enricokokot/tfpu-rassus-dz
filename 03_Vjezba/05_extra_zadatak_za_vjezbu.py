import aiohttp
import asyncio
import json

async def fetch_json_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Failed to retrieve data from {url}. Status code: {response.status}")
                return None

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3',
    ]
    
    tasks = [fetch_json_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    for i, data in enumerate(results):
        if data:
            print(f"Data from URL {urls[i]}:")
            print(f"User ID: {data['userId']}")
            print(f"ID: {data['id']}")
            print(f"Title: {data['title']}")
            print(f"Body: {data['body']}\n")

if __name__ == '__main__':
    asyncio.run(main())
