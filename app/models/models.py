from pydantic import BaseModel
from pydantic import EmailStr
from typing import Union

class User(BaseModel):
    name: str = 'John Doe'
    id: int = 1

class UserAge(BaseModel):
    name: str = 'John Doe'
    age: int = 17
    # is_adult: bool = False

class Feedback(BaseModel):
    name: str = 'Anonymous user'
    message: str = 'No message left'

class NewUser(BaseModel):
    name: str
    email: EmailStr
    age: Union[int, None] = None
    is_subscribed: bool = False

class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float