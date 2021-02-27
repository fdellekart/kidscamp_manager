from datetime import timedelta
from typing import List
import sqlite3


from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from envyaml import EnvYAML
from jose import JWTError, jwt


from database import add_applications, get_all_kids, get_all_parents
from user_management import (
    get_user,
    authenticate_user,
    create_access_token,
    User,
    TokenData,
    Token,
)
from models.applications import Kid, Parent
from exceptions import credentials_exception, unauthorized_exception
from views import applications

env = EnvYAML()

SECRET = env["secret"]
EXPIRE_MINUTES = 5

def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.db_conn = sqlite3.connect("kidscamp.db")


@app.on_event("shutdown")
async def shutdown():
    app.state.db_conn.close()


app.include_router(applications.router)


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


@app.get("/allkids/")
async def all_kids(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_kids(app.state.db_conn)
    except JWTError:
        raise credentials_exception


@app.get("/allparents/")
async def parent(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_parents(app.state.db_conn)
    except JWTError:
        raise credentials_exception


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
        raise unauthorized_exception
    access_token_expires = timedelta(minutes=EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
