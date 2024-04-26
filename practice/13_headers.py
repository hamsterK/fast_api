from typing import Annotated, Union
from fastapi import FastAPI, Header, Response

app = FastAPI()

# @app.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header()] = None): python 3.10+
#     return {"User-Agent": user_agent}

# to disable automatic conversion of headers to snake case for python => set parameter convert_underscores=False

# get User-Agent header:
@app.get("/headers-1")
def root(user_agent: str = Header()):
    return {"User-Agent": user_agent}

@app.get("/headers-2")
def root():
    data = "Hello"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123459"})

@app.get("/headers-3")
def root(response: Response):
    response.headers["Secret-Code"] = "123459"
    return {"message": "Hello again"}

# uvicorn practice.13_headers:app --reload
