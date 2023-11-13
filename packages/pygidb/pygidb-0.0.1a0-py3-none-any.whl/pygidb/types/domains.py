from typing import List, Optional

from pydantic import BaseModel


class RewardpreviewItem(BaseModel):
    name: str
    count: Optional[int] = None
    rarity: Optional[str] = None


class Domain(BaseModel):
    name: str
    region: str
    domainentrance: str
    domaintype: str
    description: str
    recommendedlevel: int
    recommendedelements: List[str]
    unlockrank: int
    rewardpreview: List[RewardpreviewItem]
    disorder: List[str]
    monsterlist: List[str]
