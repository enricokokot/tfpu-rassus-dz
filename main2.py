import fastapi

app = fastapi.FastAPI()


@app.get("/info_2")  # python dekoratori
def krumpir():
    print("unutar funkcije")

    return {
        "status": "ok",
        "server": 2,
    }  # ovo je "dict"


# uvicorn main2:app --reload --port 8001
