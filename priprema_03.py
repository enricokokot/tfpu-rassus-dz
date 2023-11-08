import random
import asyncio
import aiohttp
import json


# 01
async def print_hello_with_delay():
    random_delay = random.randint(1, 50) / 10
    print("Hello world!")
    print(f"We'll wait exactly {random_delay} seconds")
    await asyncio.sleep(random_delay)

# asyncio.run(print_hello_with_delay())


# 02
async def zadatak1():
    for percentage in range(0, 110, 10):
        await asyncio.sleep(1)
        print(f"Task 1 completed {percentage}%")

async def zadatak2():
    for percentage in range(0, 110, 10):
        await asyncio.sleep(1.5)
        print(f"Task 2 completed {percentage}%")

async def main():
    task1 = asyncio.create_task(zadatak1())
    task2 = asyncio.create_task(zadatak2())

    # await asyncio.gather(task1, task2)
    await task1
    await task2

# asyncio.run(main())


# 03
async def timeout_example():
    try:
        await asyncio.wait_for(function_to_call(), timeout=3)
    except asyncio.TimeoutError:
        print("There was a TimeoutError!")

async def function_to_call():
    await asyncio.sleep(3.1)

# asyncio.run(timeout_example())


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
