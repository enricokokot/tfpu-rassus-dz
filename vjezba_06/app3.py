import fastapi
import httpx

app = fastapi.FastAPI()

@app.get("/get_population/{country_name}")
async def talk_to_app2(country_name):
    response = httpx.get(f"https://restcountries.com/v3.1/name/{country_name}")
    response = response.json()[0]["population"]
    return response