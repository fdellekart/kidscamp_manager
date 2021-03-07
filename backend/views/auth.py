from datetime import timedelta


from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm


from models.auth import Token
from auth import authenticate_user, create_access_token
from exceptions import unauthorized_exception
from database import get_db_conn


EXPIRE_MINUTES = 30

router = APIRouter()


@router.post("/auth/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_conn = Depends(get_db_conn)):
    user = authenticate_user(form_data.username, form_data.password, db_conn)
    if not user:
        raise unauthorized_exception
    access_token_expires = timedelta(minutes=EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

