from datetime import timedelta
from typing import List
import sqlite3


from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from envyaml import EnvYAML
from jose import JWTError, jwt
from pydantic import BaseModel


from database import add_applications, get_all_kids, get_all_parents
from user_management import (
    get_user,
    authenticate_user,
    create_access_token,
    User,
    TokenData,
    Token,
)

env = EnvYAML()

SECRET = env["secret"]
EXPIRE_MINUTES = 5

db_conn = sqlite3.connect("kidscamp.db")

def fake_hash_password(password: str):
    return "fakehashed" + password


class Application(BaseModel):
    parent: list
    kids: List[tuple]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

app = FastAPI()

app.mount("/pictures", StaticFiles(directory="frontend/pictures"), name="pictures")
app.mount("/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")
app.mount("/style", StaticFiles(directory="frontend/style"), name="style")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("frontend/index.html", "r") as f:
        html_page = f.read()
    return html_page


@app.get("/login/", response_class=HTMLResponse)
async def login_page():
    with open("frontend/login.html", "r") as f:
        html_page = f.read()
    return html_page


@app.get("/overview/", response_class=HTMLResponse)
async def overview_page():
    with open("frontend/overview.html", "r") as f:
        html_page = f.read()
    return html_page


@app.post("/newapplication/")
async def new_application(application: Application):
    parent = application.parent
    kids = application.kids
    add_applications(parent, kids, db_conn)


@app.get("/allkids/")
async def all_kids(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_kids(db_conn)
    except JWTError:
        raise credentials_exception


@app.get("/allparents/")
async def parent(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_parents(db_conn)
    except JWTError:
        raise credentials_exception


def fake_decode_token(token):
    user = get_user(token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/auth/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
