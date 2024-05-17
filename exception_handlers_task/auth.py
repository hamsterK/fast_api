from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from exception import UserNotFoundException, InvalidUserDataException
from schemas import User

router = APIRouter(  # used to group path operations
    prefix="/login",  # adds prefix to all routes: => /login/login_user
    tags=["LOGIN"]  # metadata for documentation purposes
)
security = HTTPBasic()

USER_DATA = [User(**{"username": "user1", "password": "pass1"}), User(**{"username": "user2", "password": "pass2"}), User(**{"username": "user3", "password": "pass3"})]

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise UserNotFoundException(status_code=404)
    return user

def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

@router.get("/login_user")
async def login(user: User = Depends(authenticate_user)):
    return {"message": "Access granted"}

@router.post("/reg_user")
async def reg_user(user_data: User):
    if len(user_data.username) < 5 or len(user_data.password) < 5:
        raise InvalidUserDataException(status_code=400)
    USER_DATA.append(**user_data.dict())
    return {"message": "Success"}

@router.get("/me")
async def get_me(user_log: User = Depends(authenticate_user)):
    for user in USER_DATA:
        if user.username == user_log.username:
            return user
