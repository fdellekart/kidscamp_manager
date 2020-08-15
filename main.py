from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Succesfully connected."}

@app.get("/newapplication/{item}")
async def root(item):
    print(item)