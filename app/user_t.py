# example to work with pytest
from fastapi import FastAPI, HTTPException, Query
from typing import Annotated

from app.models.models import UserTest as User

app = FastAPI()

users = []


@app.post("/registration")
async def reg_user(
        username: Annotated[str, Query(...)],  #  parameter is required in the query string of the request.
        password: Annotated[str, Query(...)]
):
    for user in users:
        if user.username == username:
            raise HTTPException(status_code=409, detail="User already exists")
    users.append(User(username=username, password=password))
    return {"message": "Success!"}


@app.get("/me")
async def read_user(
        username: Annotated[str, Query(...)]
):
    for user in users:
        if user.username == username:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user")
async def delete_user(
        username: Annotated[str, Query(...)]
):
    try:
        users.remove([i for i in users if i.username == username][0])
    except:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User was removed"}

# python -m pytest
