from fastapi import FastAPI
import httpx
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from contextlib import asynccontextmanager
from pydantic import BaseModel
import asyncio
from typing import List, Optional

DATABASE_URL = "sqlite:///./baza.db"
engine = create_engine(DATABASE_URL, echo=True)
meta = MetaData()

trainers = Table(
    "trainers",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

pokemon = Table(
    "pokemon",
    meta,
    Column("id", Integer, primary_key=True),
    Column("trainer_id", Integer),
    Column("name", String),
    Column("height", String),
    Column("weight", String),
)

class Trainer(BaseModel):
    id: Optional[int] = None
    name: str

class Pokemon(BaseModel):
    id: Optional[int] = None
    trainer_id: int
    name: str
    height: int
    weight: int

async def init_db():
    meta.create_all(engine)
    conn = engine.connect()

    conn.execute(trainers.insert(), [
        {"name": "Marko"},
        {"name": "David"},
    ])

    rows = conn.execute(trainers.select())
    print("Trainers in the database after initialization:")
    for row in rows:
        print(f"    {row}")


    tasks = [fetch_pokemon(poke_id) for poke_id in [10, 20, 50]]
    pokemon_ids = await asyncio.gather(*tasks)
    conn.execute(pokemon.insert(), pokemon_ids)

    rows = conn.execute(pokemon.select())
    print("Pokemon in the database after initialization:")
    for row in rows:
        print(f"    {row}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await shutdown_db()

app = FastAPI(lifespan=lifespan)

async def shutdown_db():
    engine.dispose()

async def fetch_pokemon(pokemon_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        response = response.json()
        the_pokemon = {
            "id": pokemon_id,
            "name": response["name"],
            "height": response["height"],
            "weight": response["weight"],
        }
        return the_pokemon

@app.get("/trainer", response_model=List[Trainer])
async def read_all_trainers():
    conn = engine.connect()
    rows = conn.execute(trainers.select())
    new_trainers = [Trainer(id=trainer.id, name=trainer.name) for trainer in rows]
    return new_trainers

@app.get("/trainer/{trainer_id}", response_model=List[Trainer])
async def read_a_trainer(trainer_id):
    conn = engine.connect()
    rows = conn.execute(trainers.select().where(trainers.c.id==trainer_id))
    new_trainers = [Trainer(id=trainer.id, name=trainer.name) for trainer in rows]
    return new_trainers

@app.post("/trainer")
async def create_trainer(trainer: Trainer):
    conn = engine.connect()
    ins = trainers.insert().values(name=trainer.name)
    result = conn.execute(ins)
    return {"result": "ok"}

@app.put("/trainer/{trainer_id}")
async def update_trainer(trainer_id, trainer: Trainer):
    conn = engine.connect()
    ins = trainers.update().where(trainers.c.id == trainer_id).values(name = trainer.name)
    result = conn.execute(ins)
    return {"result": "ok"}

@app.delete("/trainer/{trainer_id}")
async def delete_trainer(trainer_id):
    conn = engine.connect()
    ins = trainers.delete().where(trainers.c.id == trainer_id)
    result = conn.execute(ins)
    return {"result": "ok"}

@app.get("/pokemon", response_model=List[Pokemon])
async def read_all_pokemon():
    conn = engine.connect()
    rows = conn.execute(pokemon.select())
    new_pokemon = [Pokemon(
        id=pokemonn.id, 
        name=pokemonn.name,
        trainer_id=pokemonn.trainer_id,
        height=pokemonn.height,
        weight=pokemonn.weight) for pokemonn in rows]
    return new_pokemon

@app.get("/pokemon/{pokemon_id}", response_model=List[Pokemon])
async def read_a_pokemon(pokemon_id):
    conn = engine.connect()
    rows = conn.execute(pokemon.select().where(pokemon.c.id==pokemon_id))
    new_pokemons = [Pokemon(
        id=pokemonn.id, 
        name=pokemonn.name,
        trainer_id=pokemonn.trainer_id,
        height=pokemonn.height,
        weight=pokemonn.weight) for pokemonn in rows]
    return new_pokemons

@app.post("/pokemon/{pokemon_id}")
async def create_pokemon(pokemon_id, trainer_idd):
    the_pokemon = await fetch_pokemon(pokemon_id)
    print(the_pokemon)
    conn = engine.connect()
    ins = pokemon.insert().values(name=the_pokemon["name"], weight=the_pokemon["weight"], height=the_pokemon["height"], trainer_id=trainer_idd)
    result = conn.execute(ins)
    return {"result": "ok"}

@app.put("/pokemon/{pokemon_id}")
async def update_pokemon(pokemon_id, pokemonn: Pokemon):
    conn = engine.connect()
    ins = pokemon.update().where(pokemon.c.id == pokemon_id).values(name = pokemonn.name)
    result = conn.execute(ins)
    return {"result": "ok"}

@app.delete("/pokemon/{pokemon_id}")
async def delete_pokemon(pokemon_id):
    conn = engine.connect()
    ins = pokemon.delete().where(pokemon.c.id == pokemon_id)
    result = conn.execute(ins)
    return {"result": "ok"}