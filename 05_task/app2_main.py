# app2.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app2 = FastAPI()


def perform_calculation(data):
    # Example: Multiply all values in the received data by 2
    result = {key: value * 2 for key, value in data.items()}
    return result


# Endpoint in app2 to communicate with app1 and perform a calculation
@app2.post("/api/app2_to_app1")
async def app2_to_app1(data: dict):
    if not data:
        raise HTTPException(status_code=400, detail="Invalid data received from app1")

    calculation_result = perform_calculation(data)
    print(calculation_result)

    return JSONResponse(content={"result_from_app1": data, "calculation_result": calculation_result})
