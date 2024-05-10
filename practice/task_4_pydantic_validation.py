from datetime import datetime
from typing import List, Union

from pydantic import BaseModel
# instead of BaseModel we can use:
# from dataclasses import dataclass + @dataclass decorator + class User(): ...

# data model usually placed in models.py
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

# external data imitating incoming json
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

# imitation of incoming data unpacking
user = User(**external_data)
print(user)
print(user.id)
