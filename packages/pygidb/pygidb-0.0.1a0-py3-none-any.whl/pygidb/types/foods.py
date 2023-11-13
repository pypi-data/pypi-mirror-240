from typing import List, Optional

from pydantic import BaseModel


class Quality(BaseModel):
    effect: str
    description: str


class Ingredient(BaseModel):
    name: str
    count: int


class Food(BaseModel):
    name: str
    rarity: str
    foodtype: str
    foodfilter: str
    foodcategory: str
    effect: str
    description: str
    basedish: Optional[str] = None
    character: Optional[str] = None
    suspicious: Optional[Quality] = None
    normal: Optional[Quality] = None
    delicious: Optional[Quality] = None
    ingredients: List[Ingredient]
