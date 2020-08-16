from typing import Optional


from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import date


app = FastAPI()


class Item(BaseModel):
    Erziehungsberechtigter: str
    mail_addr: str
    telephone: str
    Kind1: str
    kid1_bday: str
    Kind2: Optional[str]
    kid2_bday: Optional[str]
    Kind3: Optional[str]
    kid3_bday: Optional[str]
    Kind4: Optional[str]
    kid4_bday: Optional[str]


@app.get("/")
def root():
    return {"message" : "Succesfully connected."}

@app.post("/newapplication/")
def new_application(request: Request):
    print(request.json())