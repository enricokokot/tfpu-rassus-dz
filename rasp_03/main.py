import fastapi
import aiohttp
import json

app = fastapi.FastAPI()


@app.get("/zbroj_fib/{n}")
async def zbroj_fib(n):
    n = int(n)
    final_result = 0
    for i in range(n+1):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:8000/fib/" + str(i)) as response:
                result = await response.text()
                final_result += int(json.loads(result)["result"])
    return {"input": n, "result": final_result}
