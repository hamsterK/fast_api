from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from auth import router as router_login
from exception_model import ErrorResponseModel

from exception import UserNotFoundException, InvalidUserDataException
from datetime import datetime

app = FastAPI()
app.include_router(router_login)

@app.exception_handler(UserNotFoundException)
async def user_not_found(request: Request, exc: ErrorResponseModel):
    start = datetime.now()
    return JSONResponse(
        status_code=exc.status_code,
        content={"Error": exc.detail, "status_code": exc.status_code},
        headers={"X-ErrorHandleTime": str(start - datetime.now())}
    )

@app.exception_handler(InvalidUserDataException)
async def invalid_user_data(request: Request, exc: ErrorResponseModel):
    start = datetime.now()
    return JSONResponse(
        status_code=exc.status_code,
        content={"Error": exc.detail, "status_code": exc.status_code},
        headers={"X-ErrorHandleTime": str(start - datetime.now())}
    )
