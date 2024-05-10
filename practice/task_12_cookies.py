from fastapi import FastAPI, Cookie, Response
from typing import Union
from datetime import datetime

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}

@app.get("/a")
def root(last_visit = Cookie()):  # access cookie files
    return {"last visit": last_visit}

@app.get("/b")
def root(response: Response):  # set cookie for response
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    response.set_cookie(key="last_visit", value=now)
    return {"message": "cookies are set"}

"""
@router.post("/logout", status_code=204)  # delete cookies - example
async def logout_user(response: Response):
    response.delete_cookie("example_access_token")
"""
