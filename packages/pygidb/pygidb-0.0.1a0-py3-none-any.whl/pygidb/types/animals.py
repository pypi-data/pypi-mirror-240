from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    description: str
    category: str
    counttype: str
    sortorder: int
