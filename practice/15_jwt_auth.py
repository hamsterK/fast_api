import jwt

SECRET_KEY = 'mysecretkey'  # example of bash command to use instead: 'openssl rand -hex 32'
ALGORITHM = 'HS256'  # in real life expiry date is also set

# in real life, only password HASH is stored here (passlib + salt)
USERS_DATA = [
    {"username": "admin", "password": "qwerty"}
]

def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)  # encoding token here

def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass

def get_user(username: str):
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None

token = create_jwt_token({"sub": "admin"})
print(token)

username = get_user_from_token(token)
print(username)

current_user = get_user(username)
print(current_user)
