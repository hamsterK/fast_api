from pydantic import BaseModel

class User(BaseModel):
    name: str = 'John Doe'
    id: int = 1

class UserAge(BaseModel):
    name: str = 'John Doe'
    age: int = 17
    # is_adult: bool = False

