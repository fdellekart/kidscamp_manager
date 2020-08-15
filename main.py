from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    Erziehungsberechtigter: str
    mail_addr: str
    telephone: str
    Kind1: str
    kid1_bday: str
    Kind2: str
    kid2_bday: str
    Kind3: str
    kid3_bday: str
    Kind4: str
    kid4_bday: str


@app.get("/")
async def root():
    return {"message" : "Succesfully connected."}

@app.post("/newapplication/")
async def root(item: Item):
    print(item.Erziehungsberechtigter)