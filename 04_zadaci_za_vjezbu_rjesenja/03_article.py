from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int = 1

# Sample list of items
items = []

@app.post("/items/", response_model=dict)
def create_item(item: Item):
    new_item = {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "quantity": item.quantity
    }
    items.append(new_item)
    return new_item

@app.get("/get_items/", response_model=List[dict])
def get_all_items():
    return items
