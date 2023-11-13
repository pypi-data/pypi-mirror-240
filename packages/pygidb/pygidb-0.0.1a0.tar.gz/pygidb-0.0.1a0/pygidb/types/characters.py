from typing import List, Optional

from pydantic import BaseModel, Field


class Cv(BaseModel):
    english: str
    chinese: str
    japanese: str
    korean: str


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


class Images(BaseModel):
    card: Optional[str] = None
    portrait: Optional[str] = None
    icon: Optional[str] = None
    sideicon: Optional[str] = None
    cover1: Optional[str] = None
    cover2: Optional[str] = None
    hoyolab_avatar: Optional[str] = Field(None, alias='hoyolab-avatar')
    nameicon: Optional[str] = None
    nameiconcard: Optional[str] = None
    namegachasplash: Optional[str] = None
    namegachaslice: Optional[str] = None
    namesideicon: Optional[str] = None


class Base(BaseModel):
    hp: float
    attack: float
    defense: float
    critrate: float
    critdmg: float


class Curve(BaseModel):
    hp: str
    attack: str
    defense: str


class PromotionItem(BaseModel):
    maxlevel: int
    hp: float
    attack: float
    defense: float
    specialized: float


class Stats(BaseModel):
    base: Base
    curve: Curve
    specialized: str
    promotion: List[PromotionItem]


class URL(BaseModel):
    fandom: str


class Character(BaseModel):
    name: str
    fullname: str
    title: str
    description: str
    rarity: str
    element: str
    weapontype: str
    substat: str
    gender: str
    body: str
    association: str
    region: str
    affiliation: str
    birthdaymmdd: str
    birthday: str
    constellation: str
    cv: Cv
    costs: Costs
    images: Optional[Images] = None
    stats: Optional[Stats] = None
    url: Optional[URL] = None
    version: str


# Constellations
class Constellation(BaseModel):
    name: str
    effect: str


class Constellations(BaseModel):
    name: str
    c1: Constellation
    c2: Constellation
    c3: Constellation
    c4: Constellation
    c5: Constellation
    c6: Constellation


# Talents
class Attributes(BaseModel):
    labels: List[str]


class Combat(BaseModel):
    name: str
    info: str
    description: Optional[str] = None
    attributes: Attributes


class Passive(BaseModel):
    name: str
    info: str


class LvlItem(BaseModel):
    name: str
    count: int


class TalentCosts(BaseModel):
    lvl2: List[LvlItem]
    lvl3: List[LvlItem]
    lvl4: List[LvlItem]
    lvl5: List[LvlItem]
    lvl6: List[LvlItem]
    lvl7: List[LvlItem]
    lvl8: List[LvlItem]
    lvl9: List[LvlItem]
    lvl10: List[LvlItem]


class Talents(BaseModel):
    name: str
    combat1: Combat
    combat2: Combat
    combat3: Combat
    passive1: Passive
    passive2: Passive
    passive3: Passive
    costs: TalentCosts
