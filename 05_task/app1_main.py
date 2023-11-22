# app1.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app1 = FastAPI()


def perform_calculation(data):
    # Example: Sum all values in the received data
    print(data)
    result = 0
    for value in data['calculation_result']:
        print(data['calculation_result'][value])
        result = int(data['calculation_result'][value]) + result 
    return result


# Endpoint in app1 to communicate with app2 and perform a calculation
@app1.get("/api/app1_to_app2")
async def app1_to_app2():
    data_to_send = {"value1": 10, "value2": 20, "value3": 30}

    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8002/api/app2_to_app1", json=data_to_send)

    result_from_app2 = response.json()
    print(result_from_app2)
    calculation_result = perform_calculation(result_from_app2)

    return JSONResponse(content={"result_from_app2": result_from_app2['calculation_result'], "calculation_result": calculation_result})
