import os
from datetime import datetime, timedelta
from typing import Optional
from hashlib import sha256


import pandas as pd
from pydantic import BaseModel
from envyaml import EnvYAML
from passlib.context import CryptContext
from jose import jwt


env = EnvYAML()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    user = get_user(username)
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


def add_user(username: str, password: str, email: str):
    hashed_password = get_password_hash(password)
    new_user = pd.DataFrame(
        {"username": username, "hashed_password": hashed_password, "email": email},
        index=[
            0,
        ],
    )
    if os.path.exists(env["users_file"]):
        users = pd.read_csv(env["users_file"])
        if username in users["username"].values:
            print("User already exists.")
            return False
        users = users.append(new_user, ignore_index=True)
        users.to_csv(env["users_file"], index=False)
        return True
    else:
        new_user.to_csv(env["users_file"], index=False)
        return True


def get_user(username: str):
    users = pd.read_csv(env["users_file"])
    if username in users["username"].values:
        condition = users["username"] == username
        return UserInDB(**users.loc[condition, :].loc[0].to_dict())
