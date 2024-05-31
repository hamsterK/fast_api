from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.models.schemas import User
from app.dao import UsersDAO


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Reg"]
)

security = HTTPBasic()


async def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = await UsersDAO.get_user(name=credentials.username)
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user


@router.post("/login")
async def login_user(user: User = Depends(authenticate_user)):
    return user


@router.post("/reg")
async def reg_user(user_data: User):
    user = await UsersDAO.get_user(name=user_data.name)
    if user:
        raise HTTPException(status_code=409)
    await UsersDAO.add_user(user_data.name, user_data.email)
