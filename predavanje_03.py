from multiprocessing import ThreadPool
import asyncio

parametri = [i for i in range(100)]

with ThreadPool(processes=100) as pool:
    rezultat = pool.map(pozovi_fib, parametri)
# return {"input": n, "result": sum(rezultat)}

def get_fib(x):
    return x

def pozovi_fib(x):
    return x

# global interpreter lock problem in python
asyncio.gather(
    get_fib(0),
    get_fib(1),
    get_fib(2),
)

# korutina = laka dretva
