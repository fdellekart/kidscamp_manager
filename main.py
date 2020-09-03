from typing import Optional
from datetime import date


from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from pydantic import BaseModel
from envyaml import EnvYAML


from applications import resolve_application, add_applications
import user_management

env = EnvYAML()


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


@app.get("/overview/")
def overview_page(user=Depends(user_management.manager)):
    with open("frontend/overview.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    add_applications(parent, kids)


@app.post('/auth/token')
async def login(request: Request):
    body = await request.json()
    print(body)
    username = body["username"]
    password = body["password"]

    user = user_management.load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user["password"]:
        raise InvalidCredentialsException

    access_token = user_management.manager.create_access_token(
        data={"username" :  username}
    )
    return {"access_token" : access_token, "token_type" : "bearer"}
