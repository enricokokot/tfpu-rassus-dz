import fastapi
from pydantic import BaseModel, field_validator

app = fastapi.FastAPI()

class Input(BaseModel):
    data: dict

    @field_validator("data")
    def validate_data(cls, value):
        try:
            if not all(isinstance(key, str) and isinstance(value, int) for key, value in value.items()):
                raise TypeError("Invalid data format. Keys must be strings and values must be integers.")
            return value
        except TypeError as err:
            return err

@app.post("/api/app2_to_app1")
async def talk_to_app1(data: Input):
    # for item in data.items():
    #     if not "value" in item[0]:
    #         return "Error"
    #     if not isinstance(item[1], int):
    #         return "Error"
    if isinstance(data.data, TypeError):
        return str(data.data)
    new_data = {key: value*2 for key, value in data.data.items()}
    return {
        "old data": data,
        "new data": new_data
    }