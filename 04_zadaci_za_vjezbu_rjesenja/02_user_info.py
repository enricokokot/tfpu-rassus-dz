from fastapi import FastAPI, HTTPException

app = FastAPI()

user_data = {
    "johndoe": ["John", "Doe", 30, "john.doe@example.com"],
    "alicesmith": ["Alice", "Smith", 25, "alice.smith@example.com"],
    "bobjones": ["Bob", "Jones", 28, "bob.jones@example.com"],
    # Add more users as needed
}


@app.get("/user/{username}")
def read_user(username: str):
    if username in user_data:
        user_details = user_data[username]
        user_json = {
            "name": user_details[0],
            "last_name": user_details[1],
            "age": user_details[2],
            "email": user_details[3],
        }
        return user_json
    else:
        raise HTTPException(status_code=404, detail="User not found")
