from typing import List, Optional

from pydantic import BaseModel


class AscendItem(BaseModel):
    name: str
    count: int


class Costs(BaseModel):
    ascend1: List[AscendItem]
    ascend2: List[AscendItem]
    ascend3: List[AscendItem]
    ascend4: List[AscendItem]
    ascend5: List[AscendItem]
    ascend6: List[AscendItem]


class URL(BaseModel):
    fandom: str


class Images(BaseModel):
    nameicon: str
    namegacha: str
    icon: str
    nameawakenicon: str
    awakenicon: Optional[str] = None


class Base(BaseModel):
    attack: float
    specialized: float


class Curve(BaseModel):
    attack: str
    specialized: str


class PromotionItem(BaseModel):
    maxlevel: int
    attack: float


class Stats(BaseModel):
    base: Base
    curve: Curve
    specialized: str
    promotion: List[PromotionItem]


class Weapon(BaseModel):
    name: str
    description: str
    weapontype: str
    rarity: str
    story: str
    baseatk: int
    substat: str
    subvalue: str
    effectname: str
    effect: str
    r1: List[str]
    r2: List[str]
    r3: List[str]
    r4: List[str]
    r5: List[str]
    weaponmaterialtype: str
    costs: Costs
    url: Optional[URL] = None
    images: Optional[Images] = None
    stats: Optional[Stats] = None
    version: str
