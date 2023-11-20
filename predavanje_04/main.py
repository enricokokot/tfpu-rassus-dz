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
workers = []
counter = 0


@app.get("/fib/{n}")
async def zbroj_fib(n):
    global counter, workers
    n = int(n)
    if not workers:
        return {"input": n, "result": "All servers are currently busy"}
    living_workers = [worker for worker in workers if worker["alive"] == True]
    if counter >= len(living_workers):
        counter = 0
    current_worker = living_workers[counter]["port"]
    living_workers[counter]["requests"] += 1
    counter = (counter + 1) % len(living_workers)
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:" + str(current_worker) + "/fib/" + str(n)) as response:
            result = await response.json()
            final_result = int(result["result"])

    return {"input": n, "result": final_result}


@app.get("/worker")
async def vrati_workera():
    return {"status": "job completed", "answer": workers}


@app.post("/worker/{port_number}")
async def prijavi_workera(port_number):
    global workers
    worker_ports = [worker["port"] for worker in workers]
    port_number = int(port_number)
    if port_number in worker_ports:
        workers = [worker if worker["port"] != port_number else {"port": worker["port"], "alive": True, "requests": worker["requests"]} for worker in workers]
        return {"status": "job completed", "answer": workers}    
    worker = {
        "port": port_number,
        "alive": True,
        "requests": 0
    }
    workers.append(worker)
    return {"status": "job completed", "answer": workers}


@app.delete("/worker/{port_number}")
async def odjavi_workera(port_number):
    global workers
    port_number = int(port_number)
    workers = [worker if worker["port"] != port_number else {"port": worker["port"], "alive": False, "requests": worker["requests"]} for worker in workers]
    return {"status": "job completed", "answer": workers}


async def start_checking_for_workers():
    while True:
        for worker in workers:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get("http://127.0.0.1:" + str(worker["port"])) as response:
                        result = await response.json()
                except aiohttp.ClientConnectorError as err:
                    worker["alive"] = False
        print(f"Pass completed. Current status: {workers}")
        await asyncio.sleep(10)

@app.get("/admin")
async def get_workers_status():
    return workers
