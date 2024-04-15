from fastapi import FastAPI


app = FastAPI()

@app.get('/{user_id}')  # set user id
async def search_user_by_id(user_id: int):
    return{"Here is the user by id": user_id}
