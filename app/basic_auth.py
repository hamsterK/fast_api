from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasicCredentials, HTTPBasic

app = FastAPI()
security = HTTPBasic()

class User(BaseModel):
    username: str
    password: str

USER_DATA = [User(**{'username': 'admin', 'password': 'qwerty'}), User(**{'username': 'user2', 'password': 'password1!'})]

def get_user_from_db(username: str = None):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

# headers={"WWW-Authenticate": "Basic"} allows requesting new credentials after unsuccessful login
def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong login or password', headers={"WWW-Authenticate": "Basic"})
    return user

@app.get("/login")
def user_login_basic(user: User = Depends(basic_auth)):
    return {"message": "Login successful", "user_info": user}

# uvicorn app.basic_auth:app --reload
