import fastapi

app = fastapi.FastAPI()


def get_fib(a):
    return a  # izračunati fib


@app.get("/fib/{x}")  # python dekoratori
def fibonacci(x):
    x = int(x)
    return {"input": x, "result": -1}


# uvicorn main2:app --reload --port 8001
