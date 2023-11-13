from typing import List, Optional

from pydantic import BaseModel


class Playcost(BaseModel):
    costtype: str
    count: int


# Action Cards
class ActionCard(BaseModel):
    id: int
    name: str
    cardtype: str
    cardtypetext: str
    tags: List[str]
    tagstext: List[str]
    description: str
    descriptionraw: str
    descriptionreplaced: str
    storytitle: str
    storytext: str
    source: str = None
    playcost: List[Playcost]


# Card backs
class CardBack(BaseModel):
    id: int
    name: str
    description: str
    descriptionraw: str
    source: str
    rarity: int


class CardBox(BaseModel):
    id: int
    name: str
    description: str
    descriptionraw: str
    source: str
    rarity: int


# Character cards
class Skill(BaseModel):
    id: int
    name: str
    descriptionraw: str
    basedamage: Optional[int] = None
    baseelement: Optional[str] = None
    descriptionreplaced: str
    description: str
    typetag: str
    type: str
    playcost: List[Playcost]


class CharacterCard(BaseModel):
    id: int
    name: str
    hp: int
    maxenergy: int
    tags: List[str]
    tagstext: List[str]
    storytitle: str
    storytext: str
    source: str
    skills: List[Skill]


# Enemy card
class EnemyCard(BaseModel):
    id: int
    name: str
    hp: int
    maxenergy: int
    tags: List[str]
    tagstext: List[str]
    skills: List[Skill]


# Detailed rules
class Rule(BaseModel):
    title: str
    titleraw: str
    content: str
    contentraw: str
    filename_image: Optional[str] = None


class DetailedRule(BaseModel):
    id: int
    name: str
    rules: List[Rule]


# Keywords
class Keyword(BaseModel):
    id: int
    name: str
    nameraw: str
    description: str
    descriptionraw: str


# Level rewards
class Reward(BaseModel):
    id: int
    name: str
    count: int


class LevelReward(BaseModel):
    id: int
    name: str
    exp: int = None
    icontype: str
    unlockdescription: str
    unlockdescriptionraw: str
    rewards: List[Reward]


# Status effects
class StatusEffect(BaseModel):
    id: int
    name: str
    statustypetext: str
    cardtype: str
    cardtypetext: str
    tags: List[str]
    description: str
    descriptionraw: str
    descriptionreplaced: str


# Summons
class Summon(BaseModel):
    id: int
    name: str
    cardtypetext: str
    tags: List
    tagstext: List
    description: str
    descriptionraw: str
    descriptionreplaced: str
    countingtype: str
    tokentype: str
    hinttype: str

