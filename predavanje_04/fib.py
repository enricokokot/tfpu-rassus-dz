import fastapi
import aiohttp
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    id = 1
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8000/worker") as response:
            result = await response.json()
            if result["answer"] != []:
                id = result["answer"][-1] + 1
    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:8000/worker/" + str(id)) as response:
            result = await response.json()
            print(result)
    yield
    async with aiohttp.ClientSession() as session:
        async with session.delete("http://127.0.0.1:8000/worker/" + str(id)) as response:
            result = await response.json()
            print(result)

app = fastapi.FastAPI(lifespan=lifespan)


def get_fib(a):
    if a <= 1:
        return a
    else:
        return get_fib(a - 1) + get_fib(a - 2)


@app.get("/fib/{x}")  # python dekoratori
def fibonacci(x):
    x = int(x)
    result = get_fib(x)
    return {"input": x, "result": result}
