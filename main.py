from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Succesfully connected."}

@app.post("/newapplication/")
async def root(item):
    return item