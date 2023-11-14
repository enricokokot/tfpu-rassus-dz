import fastapi
from pydantic import BaseModel
import aiohttp

app = fastapi.FastAPI()

# Task 1
@app.get("/")
async def main():
    return "Hello, FastAPI!"

# Task 2
users = {
    "johndoe": {
        "name": "John",
        "last_name": "Doe",
        "age": 30,
        "email": "john.doe@example.com"
    },
    "janedoe": {
        "name": "Jane",
        "last_name": "Doe",
        "age": 24,
        "email": "jane.doe@example.com"
    },
}

@app.get("/user/{username}")
async def get_user(username):
    if username in users.keys():
        return users[username]
    return "Error: No such username!"

# Task 3
class Article(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

articles = {}

@app.post("/articles")
async def receive_article(article: Article):
    new_article_key = article.name
    new_article_body = {
        "description": article.description,
        "price": article.price,
        "quantity": article.quantity
    }
    articles[new_article_key] = new_article_body
    return article

@app.get("/get_articles")
async def return_articles():
    return [
        {
            "name": article,
            "description": articles[article]["description"],
            "price": articles[article]["price"],
            "quantity": articles[article]["quantity"]
        } 
        for article in articles.keys()]

# Task 4
class ToDo(BaseModel):
    id: int
    day: str
    task: str

todos = {}

@app.get("/todo")
async def get_todos():
    return [todo for todo in todos.values()]

@app.get("/todo/{id}")
async def get_todo(id):
    id = int(id)
    if id in todos.keys():
        return todos[id]
    return "Error: Id doesn't exist!"

@app.post("/todo")
async def add_todo(todo: ToDo):
    if todo.id in todos.keys():
        return "Error: Id already exists!"
    todos[todo.id] = todo
    return todo

# @app.put("/todo/{id}")
@app.put("/todo")
async def update_todo(todo: ToDo):
    # id = int(id)
    # if id in todos.keys():
    #     todos[id] = todo
    #     return todo
    if todo.id in todos.keys():
        todos[todo.id] = todo
        return todo
    return "Error: Id doesn't exist!"

@app.delete("/todo/{id}")
async def remove_todo(id):
    id = int(id)
    if id in todos.keys():
        removed_todo = todos.pop(id)
        return removed_todo
    return "Error: Id doesn't exist!"

# Task 5
class Pokemon(BaseModel):
    id: int
    ime: str

caught_pokemon = {"stored pokemon": {}}

@app.get("/pokemon/{id}")
async def get_pokemon(id):
    id = int(id)
    if id in caught_pokemon["stored pokemon"].keys():
        return caught_pokemon["stored pokemon"][id]
    async with aiohttp.ClientSession() as session:
        async with session.get("https://pokeapi.co/api/v2/pokemon/" + str(id)) as response:
            result = await response.json()
            final_result = {"id": result["id"], "name": result["name"], "height": result["height"]}
            # print(json.dumps(final_result, indent=2))

@app.get("/pokemon_store")
async def get_pokemons():
    return [pokemon for pokemon in caught_pokemon["stored pokemon"]]