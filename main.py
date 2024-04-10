from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # mark the function as one processing requests
async def read_root():
    return {"message": "Hello World"}

# http://localhost:8000/
# stop command in terminal: ctrl + c


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message"}
