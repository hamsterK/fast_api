from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # mark the function as one processing requests
async def root():
    return {"message": "Hello World"}

# http://localhost:8000/
# stop command in terminal: ctrl + c
