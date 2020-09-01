from typing import Optional


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import date


from applications import resolve_application, add_applications


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Succesfully connected."}


@app.get("/login/", response_class=HTMLResponse)
async def read_items():
    with open("index.html", 'r') as f:
        html_page = f.read()
    return html_page


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    add_applications(parent, kids)

