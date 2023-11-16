import fastapi
import aiohttp
from contextlib import asynccontextmanager
import asyncio


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    task = asyncio.create_task(start_checking_for_workers())
    yield
    task.cancel()

app = fastapi.FastAPI(lifespan=lifespan)
workers = set()
counter = 0


@app.get("/fib/{n}")
async def zbroj_fib(n):
    global counter
    n = int(n)
    if not workers:
        return {"input": n, "result": "All servers are currently busy"}
    counter = (counter + 1) % len(workers)
    current_worker = counter + 1
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:800" + str(current_worker) + "/fib/" + str(n)) as response:
            result = await response.json()
            final_result = int(result["result"])

    return {"input": n, "result": final_result}


@app.get("/worker")
async def vrati_workera():
    global workers
    return {"status": "job completed", "answer": workers}


@app.post("/worker/{id}")
async def prijavi_workera(id):
    global workers
    id = int(id)
    workers.add(id)
    return {"status": "job completed", "answer": workers}


@app.delete("/worker/{id}")
async def odjavi_workera(id):
    global workers
    id = int(id)
    workers.remove(id)
    return {"status": "job completed", "answer": workers}


async def start_checking_for_workers():
    while True:
        for worker in workers:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get("http://127.0.0.1:800" + str(worker)) as response:
                        result = await response.json()
                except aiohttp.ClientConnectorError as err:
                    workers.remove(worker)
        print(f"Pass completed. Current status: {workers}")
        await asyncio.sleep(10)
