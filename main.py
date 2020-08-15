from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    Name: str
    E-Mail-Adresse: str
    Nachricht: str


@app.get("/")
async def root():
    return {"message" : "Succesfully connected."}

@app.post("/newapplication/")
async def root(item: Item):
    print(item)