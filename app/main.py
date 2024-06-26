from fastapi import FastAPI
from app.models.models import User, UserAge, Feedback, NewUser, Product
from typing import Union

app = FastAPI()

fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

fake_feedbacks = list()



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
async def read_users(limit: int = 10):
    return dict(list(fake_users.items())[:limit])

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}

@app.post("/user")
async def add_user_age(user: UserAge):
    is_adult = True if user.age >= 18 else False
    return {**user.model_dump(), "is_adult": is_adult}

@app.post("/test")
async def test_endpoint():
    return {"message": "Test endpoint reached successfully"}

@app.post("/feedback")
async def send_feedback(feedback: Feedback):
    fake_feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}

@app.get("/feedbacks")
async def return_feedbacks():
    return fake_feedbacks

@app.post("/create_user")
async def create_user(user: NewUser):
    fake_users[len(fake_users) + 1] = dict(user)
    return user

# uvicorn app.main:app --reload
# npx kill-port 8000

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"John Doe\", \"age\": 25}" http://localhost:8000/user
