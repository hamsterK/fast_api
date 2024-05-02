from rbac_task.models.models import User, Role
from typing import Union

USER_DATA = {}

def get_user(uername: str) -> Union[User, None]:
    if username in  USER_DATA:
        return User(**USER_DATA[username])
    return None
