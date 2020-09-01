from typing import Optional


from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import date


from applications import resolve_application, add_applications


app = FastAPI()

app.mount("/pictures", StaticFiles(directory="frontend/pictures"), name="pictures")
app.mount("/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")
app.mount("/style", StaticFiles(directory="frontend/style"), name="style")


@app.get("/")
async def root():
    return {"message": "Succesfully connected."}


@app.get("/login/", response_class=HTMLResponse)
async def login():
    with open("frontend/index.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    add_applications(parent, kids)

