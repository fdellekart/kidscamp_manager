from typing import Optional


from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import date


from applications import resolve_application


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Succesfully connected."}


@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    parent, kids = resolve_application(request_body)
    print(parent)
    print(kids)
