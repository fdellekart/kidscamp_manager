from datetime import datetime, timedelta
from typing import Optional


from fastapi.security import OAuth2PasswordBearer
from envyaml import EnvYAML
from jose import jwt


from database.users import get_user, verify_password


env = EnvYAML()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def authenticate_user(username: str, password: str, db_conn):
    user = get_user(username, db_conn)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, env["secret"], "HS256")
    return encoded_jwt
