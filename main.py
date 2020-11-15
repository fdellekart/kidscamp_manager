from typing import Optional
from datetime import date


from fastapi import FastAPI, Request, Response, Depends, Cookie, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

app.mount("/pictures", StaticFiles(directory="frontend/pictures"), name="pictures")
app.mount("/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")
app.mount("/style", StaticFiles(directory="frontend/style"), name="style")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

@app.get("/")
async def root():
    return {"message": "Succesfully connected."}


@app.get("/login/", response_class=HTMLResponse)
async def login_page():
    with open("frontend/index.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.get("/overview/")
async def overview_page(token: str = Depends(oauth2_scheme)):
    with open("frontend/overview.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    add_applications(parent, kids)

def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
    )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user))
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post('/auth/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
   user_dict = fake_users_db.get(form_data.username)
   if not user_dict:
       raise HTTPException(status_code=400, detail="Incorrect username or password!")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password!")

    return {"access_token": user.username, "token_type": "bearer"}
