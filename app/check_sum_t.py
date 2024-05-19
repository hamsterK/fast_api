# app to check pytest
from fastapi import FastAPI
app = FastAPI()

@app.get("/sum/")
def calculate_sum(a: int, b: int):
    return {"result": a + b}

# uvicorn app.check_sum_t:app --reload
