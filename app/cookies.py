from fastapi import FastAPI, Cookie, Response, status, HTTPException
from pydantic import BaseModel
from uuid import uuid1

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

users = [{"username": "admin", "password": "qwerty", "cookie": ''}, {"username": "admin2", "password": "qwerty2", "cookie": ''}]
sessions = dict()

@app.get("/login")
async def login(user: User, response: Response):
    for i in users:
        if user.username == i["username"] and user.password == i["password"]:
            session_token = str(uuid1())
            sessions[session_token] = user
            response.set_cookie(key="session_token", value=session_token, httponly=True)
            return {"message": "successful login"}
    return {"message": "Invalid username or password"}

@app.get("/user")
async def user_info(session_token = Cookie()):
    user = sessions.get(session_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized")
    return user

# uvicorn app.cookies:app --reload