import fastapi
import aiohttp
import json

app = fastapi.FastAPI()
workers = [1, 2, 3, 4]
current_worker = 0

@app.get("/fib/{n}")
async def zbroj_fib(n):
    global current_worker
    n = int(n)
    curr_work = workers[current_worker]
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:800" + str(curr_work) + "/fib/" + str(n)) as response:
            current_worker += 1
            result = await response.text()
            final_result = int(json.loads(result)["result"])
            
    return {"input": n, "result": final_result}
