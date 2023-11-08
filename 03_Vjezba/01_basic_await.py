import asyncio
import random

async def hello_world():
    print("Hello, world!")
    sleep_interval = random.uniform(1, 5)
    await asyncio.sleep(sleep_interval)

asyncio.run(hello_world())

