from typing import Optional


from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import date


app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Succesfully connected."}

@app.post("/newapplication/")
async def new_application(request: Request):
    request_body = await request.json()
    print(request_body)
    print(type(request_body))