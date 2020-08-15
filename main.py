from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date


app = FastAPI()


class Item(BaseModel):
    Erziehungsberechtigter: str
    mail_addr: str
    telephone: int
    Kind1: str
    kid1_bday: date
    Kind2: str
    kid2_bday: date
    Kind3: str
    kid3_bday: date
    Kind4: str
    kid4_bday: date


@app.get("/")
async def root():
    return {"message" : "Succesfully connected."}

@app.post("/newapplication/")
async def root(item: Item):
    print(item.Erziehungsberechtigter)