from typing import Optional


from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from datetime import date


from applications import resolve_application, add_applications


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Succesfully connected."}


@app.get("/login/", response_class=HTMLResponse)
async def login():
    with open("index.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.get("/login/frontend/style/style.css")
async def login_style():
    return FileResponse("frontend/style/style.css")


@app.get("/login/frontend/scripts/script.js")
async def login_script():
    return FileResponse("frontend/scripts/script.js")


@app.get("/login/frontend/pictures/Logo_farb.gif")
async def login_script():
    return FileResponse("frontend/pictures/Logo_farb.gif")


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    add_applications(parent, kids)

