from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    mail: str


class UserInDB(User):
    hashed_password: str