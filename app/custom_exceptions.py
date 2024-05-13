from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# model
class ErrorResponse(BaseModel):
    status_code: int
    detail: str

# main
app = FastAPI()

class CustomExceptionA(HTTPException):
    def __init__(self, detail: str, status_code: int = 500):
        super().__init__(detail=detail, status_code=status_code)

class CustomExceptionB(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(detail=detail, status_code=status_code)

@app.exception_handler(CustomExceptionA)
async def custom_exception_handler_a(request: Request, exc: ErrorResponse):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.exception_handler(CustomExceptionB)
async def custom_exception_handler_b(request: Request, exc: ErrorResponse):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 5:
        raise CustomExceptionA(detail="Server is down", status_code=500)
    return {"item_id": item_id}

@app.get("/clients/{client_id}")
async def read_client(client_id: int):
    if client_id == 7:
        raise CustomExceptionB(detail="Not found", status_code=404)
    return {"client_id": client_id}

# uvicorn app.custom_exceptions:app --reload
