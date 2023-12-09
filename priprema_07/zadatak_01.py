from typing import List, Optional
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel


DATABASE_URL = "sqlite:///./dbs/test.db"
engine = create_engine(DATABASE_URL, echo=True)
meta = MetaData()

items = Table(
    "items",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await shutdown_db()

app = FastAPI(lifespan=lifespan)


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str


@app.get("/item", response_model=List[Item])
async def read_items():
    conn = engine.connect()
    rows = conn.execute(items.select())
    return rows


@app.post("/item", response_model=Item)
async def create_item(item: Item):
    conn = engine.connect()
    ins = items.insert().values(name=item.name, description=item.description)
    result = conn.execute(ins)
    return item


async def init_db():
    # meta.bind = engine
    meta.create_all(engine)
    conn = engine.connect()

    conn.execute(items.insert(), [
        {"name": "Initial Item 1", "description": "Description for Initial Item 1"},
        {"name": "Initial Item 2", "description": "Description for Initial Item 2"},
    ])

    rows = conn.execute(items.select())
    print("Items in the database after initialization:")
    for row in rows:
        print(f"    {row}")


async def shutdown_db():
    # conn = engine.connect()
    # await conn.execute(items.drop())
    engine.dispose()
