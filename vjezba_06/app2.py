import fastapi
import httpx
from pydantic import BaseModel

app = fastapi.FastAPI()

class CountryName(BaseModel):
    data: str

@app.post("/get_population")
async def talk_to_app2(country_name: CountryName):
    country_name = country_name.data
    response = httpx.get(f"http://127.0.0.1:8002/get_population/{country_name}")
    response = response.json()
    new_response = response * 2
    return {"original": response, "new": new_response}