from typing import List, Optional

from pydantic import BaseModel


class RecipeItem(BaseModel):
    name: str
    count: int


class Craft(BaseModel):
    name: str
    filter: str
    sortorder: int
    unlockrank: int
    resultcount: int
    moracost: Optional[int] = 0
    recipe: List[RecipeItem]
