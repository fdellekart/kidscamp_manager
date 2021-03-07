# import sqlite3


from fastapi import FastAPI


from views import applications, auth, users


app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     app.state.db_conn = sqlite3.connect("kidscamp.db")


# @app.on_event("shutdown")
# async def shutdown():
#     app.state.db_conn.close()


app.include_router(applications.router)
app.include_router(auth.router)
app.include_router(users.router)
