from fastapi import APIRouter, HTTPException, status

from rbac_task.models.models import AuthRequest, User
from rbac_task.security.security import authenticate_user, create_jwt_token

auth = APIRouter()

@auth.post("/login")
async def login(user: AuthRequest) -> dict:
    authenticated_user: User = authenticate_user(user.username, user.password)
    if authenticated_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": create_jwt_token(authenticated_user),
            "token_type": "bearer"}
