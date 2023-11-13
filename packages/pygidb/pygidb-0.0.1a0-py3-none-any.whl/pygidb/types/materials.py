from typing import List

from pydantic import BaseModel


class Material(BaseModel):
    name: str
    description: str
    sortorder: int
    rarity: str
    category: str
    materialtype: str
    source: List[str]
