from fastapi import APIRouter, Depends, HTTPException, status

from rbac_task.models.models import AuthUser, Role
from rbac_task.security.security import get_authuser_from_token

resource = APIRouter()

@resource.get("/admin/")
def get_admin_info(auth_user: AuthUser = Depends(get_authuser_from_token)) -> dict:
    if auth_user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": f"Hello adming {auth_user.username}!"}

@resource.get("/user/")
def get_user_info(auth_user: AuthUser = Depends(get_authuser_from_token)):
    if auth_user.role != Role.USER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": f"Hello user {auth_user.username}!"}

@resource.get("/protected_resource/")
def get_info(auth_user: AuthUser = Depends(get_authuser_from_token)):
    if auth_user.role not in [Role.ADMIN, Role.USER]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return {"message": f"Hello user {auth_user.username}!", "data": "sensitive data"}

@resource.get("/info/")
def get_info(auth_user: AuthUser = Depends(get_authuser_from_token)):
    return {"message": f"Hello {auth_user.username}!"}
