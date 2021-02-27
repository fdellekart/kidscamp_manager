from typing import List


from fastapi import APIRouter, Request, Depends
from jose import jwt, JWTError
from envyaml import EnvYAML


from models.applications import Application
from database.applications import add_applications
from database.kids import get_all_kids
from database.parents import get_all_parents
from auth import oauth2_scheme
from exceptions import credentials_exception

env = EnvYAML()

SECRET = env["secret"]


router = APIRouter()

@router.post("/newapplication/")
async def new_application(request: Request):
    body = await request.json()
    application = Application(**body)
    add_applications(application.parent, application.kids, request.app.state.db_conn)


@router.get("/allkids/")
async def all_kids(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_kids(token.state.db_conn)
    except JWTError:
        raise credentials_exception


@router.get("/allparents/")
async def parent(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_parents(token.state.db_conn)
    except JWTError:
        raise credentials_exception
