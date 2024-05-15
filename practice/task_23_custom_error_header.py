from fastapi import FastAPI, HTTPException
app = FastAPI()

items = {"example": "example 1"}

@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "Custom error"},
        )
    return {"item": items[item_id]}
