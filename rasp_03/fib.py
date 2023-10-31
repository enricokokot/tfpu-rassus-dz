import fastapi
from functools import lru_cache

app = fastapi.FastAPI()

@lru_cache(maxsize=None)
def get_fib(a):
    if a <= 1:
        return a
    else:
        return get_fib(a - 1) + get_fib(a - 2)


@app.get("/fib/{x}")  # python dekoratori
def fibonacci(x):
    x = int(x)
    return {"input": x, "result": get_fib(x)}


# uvicorn main2:app --reload --port 8001

# for examplary_number in [1, 2, 3, 10, 20]:
#     print(f"fib({examplary_number}) == {get_fib(examplary_number)}")

# assert get_fib(1) == 1
# assert get_fib(2) == 1
# assert get_fib(3) == 2
# assert get_fib(10) == 55
# assert get_fib(20) == 6765
