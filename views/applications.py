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
from database import get_db_conn

env = EnvYAML()

SECRET = env["secret"]


router = APIRouter()

@router.post("/newapplication/")
async def new_application(request: Request):
    body = await request.json()
    application = Application(**body)
    add_applications(application.parent, application.kids, get_db_conn())


@router.get("/allkids/")
async def all_kids(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_kids(get_db_conn())
    except JWTError:
        raise credentials_exception


@router.get("/allparents/")
async def parent(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return get_all_parents(get_db_conn())
    except JWTError:
        raise credentials_exception
