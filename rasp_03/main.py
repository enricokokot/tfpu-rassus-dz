import fastapi

app = fastapi.FastAPI()


@app.get("/zbroj_fib/{n}")
async def zbroj_fib(n):
    # pozivati drugi servis da bi izračunala sumu prvih
    # N fib brojeva
    n = int(n)
    # npr. primi 3 kao argument
    # mora vratiti fib(1) + fib(2) + fib(3)
    # primi 10 kao argument
    # mora vratiti fib(1) + fib(2) + ... + fib(10)
    # prevedeno        1  +     2  + ... +     55

    return {"input": n, "result": n}
