import fastapi

app = fastapi.FastAPI()

def get_fib(a):
    if a <= 1:
        return a
    else:
        return get_fib(a - 1) + get_fib(a - 2)


@app.get("/fib/{x}")  # python dekoratori
def fibonacci(x):
    x = int(x)
    result = get_fib(x)
    return {"input": x, "result": result}
