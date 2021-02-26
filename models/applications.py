from typing import List


from pydantic import BaseModel


class Application(BaseModel):
    kids: List[list]
    parent: list