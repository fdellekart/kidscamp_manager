import os


import pandas as pd
from envyaml import EnvYAML


env = EnvYAML()


def add_user(username: str, password: str):
    new_user = pd.DataFrame({"username" : username, "password" : password}, index=[1,])
    if os.path.exists(env["users_file"]):
        users = pd.read_csv(env["users_file"])
        if username in users["username"].values:
            return False
        users = users.append(new_user, ignore_index=True)
        users.to_csv(env["users_file"], index=False)
        return True
    else:
        new_user.to_csv(env["users_file"], index=False)
        return True
