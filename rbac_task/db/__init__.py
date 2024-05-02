from rbac_task.security.pwdcrypt import encode_password
from rbac_task.models.models import User, Role
from rbac_task.db.db import USER_DATA

USER_DATA["admin"] = {"username": "admin", "password": encode_password("admin"), "role": Role.ADMIN}
USER_DATA["user"] = {"username": "user", "password": encode_password("password"), "role": Role.USER}
USER_DATA["guest"] = {"username": "guest", "password": encode_password("12345"), "role": Role.GUEST}
