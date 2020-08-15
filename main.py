from fastapi import FastAPI


app = FastAPI()


@app.get("/kids/{first_name}")
async def root(first_name: str):
    return {"first_name" : first_name}