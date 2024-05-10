from fastapi import FastAPI
from pydantic import BaseModel
# instead of BaseModel we can use:
# from dataclasses import dataclass + @dataclass decorator + class User(): ...

app = FastAPI()

class User(BaseModel):
    username: str
    message: str

external_data = {
    "username": "bunny",
    "message": "Hi there",
}

user = User(**external_data)

@app.post("/")
async def root(user: User):
    print(f'Message received from user {user.username}: {user.message}')
    return user
