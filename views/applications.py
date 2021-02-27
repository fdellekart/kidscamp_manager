from typing import List


from fastapi import APIRouter, Request


from models.applications import Application
from database import add_applications


router = APIRouter()


@router.post("/newapplication/")
async def new_application(request: Request):
    body = await request.json()
    application = Application(**body)
    add_applications(application.parent, application.kids, request.app.state.db_conn)