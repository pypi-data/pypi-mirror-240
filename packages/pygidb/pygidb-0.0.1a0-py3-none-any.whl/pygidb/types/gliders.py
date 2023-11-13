from typing import List

from pydantic import BaseModel


class Glider(BaseModel):
    name: str
    description: str
    rarity: str
    story: str
    sortorder: int
    source: List[str]