from pydantic import BaseModel, ConfigDict

class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

class Todo(TodoCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
