from typing import Optional
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserModel(BaseModel):
    username: str
    age: int = Field(gt=18)
    email: EmailStr
    password: str = Field(min_length=8, max_length=16)
    phone: Optional[str] = "Unknown"

custom_messages = {
    "username": "Name must be a string",
    "age": "Age must be 18 and above",
    "email": "Wrong email format",
    "password": "Password length must be from 8 to 16 symbols",
    "phone": "phone must be a string",
}

@app.exception_handler(RequestValidationError)
def custom_request_validation_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = error["loc"][-1]
        msg = custom_messages.get(field)
        errors.append({"field": field, "msg": msg, "value": error["input"]})
    print(errors)
    return JSONResponse(status_code=400, content=errors)

@app.post("/users/")
async def post_user(user: UserModel):
    return user

# uvicorn app.error_processing:app --reload
