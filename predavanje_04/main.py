import fastapi
import aiohttp
from contextlib import asynccontextmanager
import asyncio
import sys
import subprocess
import json

workers = []
counter = 0


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    global workers
    if "--port" in sys.argv:
        port_index = sys.argv.index("--port") + 1
        if port_index < len(sys.argv):
            port_number = int(sys.argv[port_index])
        if port_number == 8000:
            with open('workers.json', 'r') as openfile:
                workers = json.load(openfile)
            task = asyncio.create_task(start_checking_for_workers())
        else:
            task = asyncio.create_task(start_checking_balancer_heartbeat())
    yield
    task.cancel()

app = fastapi.FastAPI(lifespan=lifespan)


@app.get("/worker")
async def vrati_workera():
    return {"status": "job completed", "answer": workers}


@app.post("/worker/{port_number}")
async def prijavi_workera(port_number):
    global workers
    worker_ports = [worker["port"] for worker in workers]
    port_number = int(port_number)
    if port_number in worker_ports:
        workers = [worker if worker["port"] != port_number else {
            "port": worker["port"], "alive": True, "requests": worker["requests"]} for worker in workers]
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
    workers = [worker if worker["port"] != port_number else {
        "port": worker["port"], "alive": False, "requests": worker["requests"]} for worker in workers]
    return {"status": "job completed", "answer": workers}


@app.get("/admin")
async def get_workers_status():
    return workers


@app.get("/{route:path}")
async def generic_get_load_balance(route):
    global counter, workers
    living_workers = [worker for worker in workers if worker["alive"] == True]
    if not living_workers:
        return {"result": "All servers are currently busy"}
    if counter >= len(living_workers):
        counter = 0
    current_worker = living_workers[counter]["port"]
    living_workers[counter]["requests"] += 1
    counter = (counter + 1) % len(living_workers)
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:" + str(current_worker) + "/" + route) as response:
            result = await response.json()
    return result


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


async def start_checking_balancer_heartbeat():
    sleep_time = 1
    while True:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("http://127.0.0.1:8000/admin") as response:
                    result = await response.json()
                    sleep_time = 1
                    with open("workers.json", "w") as outfile:
                        outfile.write(json.dumps(result, indent=4))
            except aiohttp.ClientConnectorError as err:
                sleep_time *= 2
                if sleep_time >= 16:
                    subprocess.run("uvicorn main:app --reload --port 8000")
        await asyncio.sleep(sleep_time)
