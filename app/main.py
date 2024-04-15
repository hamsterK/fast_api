from fastapi import FastAPI
from app.models.models import User, UserAge

app = FastAPI()


@app.get('/')  # mark the function as one processing requests
async def read_root():
    return {"message": "Hello World"}

# http://localhost:8000/
# stop command in terminal: ctrl + c


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message"}


# my_user = User(name='John Doe', id=1)

@app.get("/users")
async def get_user_info():
    return User

@app.post("/user")
async def add_user(user: UserAge):
    is_adult = True if user.age >= 18 else False
    return {**user.model_dump(), "is_adult": is_adult}

@app.post("/test")
async def test_endpoint():
    return {"message": "Test endpoint reached successfully"}


# uvicorn app.main:app --reload
# npx kill-port 8000

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"John Doe\", \"age\": 25}" http://localhost:8000/user
