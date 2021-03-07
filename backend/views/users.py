from fastapi import Depends, APIRouter
from envyaml import EnvYAML
from jose import jwt, JWTError


from auth import oauth2_scheme
from exceptions import credentials_exception
from models.auth import TokenData
from models.users import User
from database.users import get_user

env = EnvYAML()
SECRET = env["secret"]


router = APIRouter()


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user