import fastapi
from fastapi import HTTPException
from pydantic import BaseModel
import aiohttp

app = fastapi.FastAPI()

class Country(BaseModel):
    id: str
    ime_drzave: str
    glavni_grad: str
    clanica_un: bool
    regija: str
    podregija: str


stored_countries = {}

@app.get("/country/{country_name}")
async def get_country(country_name):
    global stored_countries
    if country_name in stored_countries.keys():
        return stored_countries[country_name]
    async with aiohttp.ClientSession() as session:
        async with session.get("https://restcountries.com/v3.1/name/" + country_name) as response:
            whole_country = await response.json()
            whole_country = whole_country[0]
            new_country = Country(id = whole_country["name"]["common"], ime_drzave = whole_country["name"]["common"], glavni_grad = whole_country["capital"][0], clanica_un = whole_country["unMember"], regija = whole_country["region"], podregija = whole_country["subregion"])
            stored_countries[country_name] = new_country
            print(stored_countries)
            return new_country

@app.get("/get_countries")
async def get_countries():
    global stored_countries
    return stored_countries

@app.delete("/delete_country/{id}")
async def delete_country(id):
    if id in stored_countries.keys():
        return stored_countries.pop(id)
    raise HTTPException(status_code=404, detail="No such country!")