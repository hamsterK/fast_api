from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, validator, Field, field_validator


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

# option 1
@app.post("/items/")
async def create_item(item: Item):
    try:
        if item.price <= 0:
            raise ValueError("Price must be above 0")
        return {"message": "Item created successfully", "item": item}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

# option 2
@app.exception_handler(ValueError)  # custom handler
async def value_error_handler(request, exc):
    return JSONResponse(status_code=400, content={"error": str(exc)})

@app.post("/items/")
async def create_item(item: Item):
    try:
        if item.price <= 0:
            raise ValueError("Price must be above 0")
        return {"message": "Item created successfully", "item": item}
    except ValueError as ve:
        raise ve

# option 3
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc)},
    )

async def custom_request_validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Custom Request Validation Error", "errors": exc.errors()},
    )

app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, custom_request_validation_exception_handler)

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be above 0")
    return {"message": "Item created successfully", "item": item}

# option 4
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    @field_validator("price")  # pydantic v2 style
    @classmethod
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be above 0")
        return value

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}
