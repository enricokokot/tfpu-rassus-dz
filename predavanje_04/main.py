import fastapi
import aiohttp

app = fastapi.FastAPI()
workers = set()
current_worker = 0


@app.get("/fib/{n}")
async def zbroj_fib(n):
    global current_worker
    n = int(n)
    curr_work = workers[current_worker]
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:800" + str(curr_work) + "/fib/" + str(n)) as response:
            current_worker += 1
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
