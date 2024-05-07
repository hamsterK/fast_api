from fastapi import FastAPI, status, HTTPException
from postgresql_sqlalchemy.models import TodoCreate
from postgresql_sqlalchemy.db_conf import add_todo, get_todo, update_todo, delete_todo
from functools import wraps

app = FastAPI()

def check_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="Todo with such id does not exist")
        return result
    return wrapper

@app.post("/create_todo")
def create(todo_data: TodoCreate):
    return add_todo(todo_data)

@app.get("/get/{todo_id}")
@check_decorator
def get(todo_id: int):
    return get_todo(todo_id)

@app.patch("/update/{todo_id}")
@check_decorator
def update(todo_id: int, data: TodoCreate):
    return update_todo(todo_id, data)

@app.delete("/delete/{todo_id}")
@check_decorator
def delete(todo_id: int):
    if delete_todo(todo_id):
        return HTTPException(status_code=status.HTTP_200_OK, detail="Todo is deleted")

# uvicorn postgresql_sqlalchemy.main:app --reload
# if __name__ == "__main__":
# uvicorn.run(app, host='127.0.0.1', port=8000)

# pgAdmin