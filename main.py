# komentari: zgodni web frameworci
# 1) aiohttp
# 2) fastapi

# instalirati python (3.10+) i pip koji ide uz taj python

# pip install aiohttp (skroz asinkrono)
# pip install fastapi --user
# python -m pip install fastapi --user

import fastapi

app = fastapi.FastAPI()

# koristit ćemo "uvicorn" za pokretanje
# python -m pip install uvicorn --user

# pokretanje: uvicorn main:app --reload


# definiranje HTTP rute s odgovorom
@app.get("/info")  # python dekoratori
def krumpir():
    print("unutar funkcije")

    return {
        "status": "ok",
        "lista": [1, 2, 3, {"ok": "not"}],
        "boolean": True,
    }  # ovo je "dict"


@app.get("/")
async def banana():
    return "Živ sam"


@app.get("/rasp")
def banana2():
    ...

    # TODO: moram pozvati onaj drugi server da bi korisniku vratio odgovor
