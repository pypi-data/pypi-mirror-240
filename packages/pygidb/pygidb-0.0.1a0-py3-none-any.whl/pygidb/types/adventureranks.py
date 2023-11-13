from typing import List, Optional

from pydantic import BaseModel


class RewardItem(BaseModel):
    name: str
    count: int
    type: str


class AdventureRank(BaseModel):
    name: str
    exp: Optional[int] = 0
    unlockdescription: str
    reward: List[RewardItem]
