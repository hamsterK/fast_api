from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post("/items/")
async def create_item(item: Item) -> Item:  # added pydantic model to check all requests
    return item

@app.get("/items/")
async def read_items() -> list[Item]:  # marked what will be returned
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
]
