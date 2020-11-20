import os
from datetime import datetime
from typing import Optional
from hashlib import sha256


import pandas as pd
from pydantic import BaseModel
from envyaml import EnvYAML


env = EnvYAML()


class User(BaseModel):
    username: str
    email: str

class UserInDB(User):
    hashed_password: str


def hash_password(password: str):
    return sha256(password.encode("utf-8")).hexdigest()

def add_user(username: str, password: str, email: str):
    hashed_password = hash_password(password)
    new_user = pd.DataFrame({"username" : username, "hashed_password" : hashed_password, "email" : email}, index=[0,])
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
