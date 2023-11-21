import fastapi
import httpx

app = fastapi.FastAPI()

data_to_send = {
    "value1": 10,
    "value2": 20,
    "value3": 30,
    }

@app.get("/api/app1_to_app2")
async def talk_to_app2():
    response = httpx.post("http://127.0.0.1:8001/api/app2_to_app1", json={"data": data_to_send})
    response = response.json()
    if isinstance(response, str):
        return response
    return {
        "result_from_app2": response["new data"],
        "calculation_result": sum(response["new data"].values())
    }