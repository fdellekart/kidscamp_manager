from typing import Optional
from datetime import date


from fastapi import FastAPI, Request, Response, Depends, Cookie
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from pydantic import BaseModel
from envyaml import EnvYAML
import pandas as pd


from applications import resolve_application, add_applications
import user_management

env = EnvYAML()

SECRET = env["secret"]
print(SECRET)

manager = LoginManager(SECRET, tokenUrl="/auth/token", use_cookie=True)

app = FastAPI()

app.mount("/pictures", StaticFiles(directory="frontend/pictures"), name="pictures")
app.mount("/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")
app.mount("/style", StaticFiles(directory="frontend/style"), name="style")


@app.get("/")
async def root():
    return {"message": "Succesfully connected."}


@app.get("/login/", response_class=HTMLResponse)
async def login_page():
    with open("frontend/index.html", 'r') as f:
        html_page = f.read()
    return html_page


<<<<<<< HEAD
@app.get("/overview/", response_class=HTMLResponse)
def overview_page(access_token: Optional[str] = Cookie(None)):
    print(access_token)
=======
@app.get("/overview/")
async def overview_page(user=Depends(manager)):
>>>>>>> new_branch
    with open("frontend/overview.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    add_applications(parent, kids)


@manager.user_loader
def load_user(username: str):
    users = pd.read_csv(env["users_file"])
    if username not in users["username"].values:
        return False
    else:
        condition = users["username"] == username
        password = users.loc[condition, "password"].values[0]
        return {"username" : username, "password" : password}


@app.post('/auth/token')
async def login(request: Request):
    body = await request.json()
    print(body)
    username = body["username"]
    password = body["password"]

    user = load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user["password"]:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=username)
    )
    return {"access_token" : access_token, "token_type" : "bearer"}
