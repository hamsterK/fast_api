import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta
from secrets import token_urlsafe
from passlib.context import CryptContext

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY = token_urlsafe(16)
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=3)
# bcrypt = hashing algorithm, deprecated-auto = upgrade password hashes automatically when deprecated
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

USERS_DATA = [
    {"username": "admin", "password": "adminpass"}
]
for dd in USERS_DATA:
    dd["password"] = pwd_context.hash(dd["password"])

class User(BaseModel):
    username: str
    password: str

def authenticate_user(username: str, password: str) -> bool:
    for user in USERS_DATA:
        if user["username"] == username:
            return pwd_context.verify(password, user["password"])
    return False

def create_jwt_token(data: dict):
    data.update({"exp": datetime.utcnow() + EXPIRATION_TIME})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="The token has expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
async def login(user_in: User):
    if authenticate_user(user_in.username, user_in.password):
        return {"access_token": create_jwt_token({"sub": user_in.username}), "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/protected_resource")
async def about_me(verified_user: dict = Depends(verify_jwt_token)):
    if verified_user:
        return {'message': 'Access to the protected resource is allowed'}

# uvicorn app.jwt_auth:app --reload
