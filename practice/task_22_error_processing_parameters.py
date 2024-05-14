from fastapi import FastAPI
from typing import Union, Annotated
app = FastAPI()

# query
@app.get("/items/")
async def read_items(q: Union[str, None] = None):  # validate and set the value here
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# path
@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], "Header"] = None):
    return {"User-Agent": user_agent}
