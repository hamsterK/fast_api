from fastapi import FastAPI
from app.models.models import User

app = FastAPI()


@app.get('/')  # mark the function as one processing requests
async def read_root():
    return {"message": "Hello World"}

# http://localhost:8000/
# stop command in terminal: ctrl + c


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message"}


user = User(name='John Doe', id=1)

@app.get('/users')
async def get_user_info(user_name: user):
    return user_name
