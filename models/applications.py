from typing import List
from datetime import date


from pydantic import BaseModel


class Kid(BaseModel):
    id: int
    parent_id: int
    first_name: str
    last_name: str
    birthday: date


class Application(BaseModel):
    kids: List[Kid]
    parent: list
