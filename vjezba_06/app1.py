import fastapi
import httpx

app = fastapi.FastAPI()

@app.get("/{country_name}")
async def talk_to_app2(country_name):
    response = httpx.post("http://127.0.0.1:8001/get_population", json={"data":country_name})
    response = response.json()
    return response
    