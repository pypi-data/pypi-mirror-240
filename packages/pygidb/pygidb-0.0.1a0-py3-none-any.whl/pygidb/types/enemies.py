from typing import List, Optional

from pydantic import BaseModel


class RewardpreviewItem(BaseModel):
    name: str
    count: Optional[float] = None
    rarity: Optional[str] = None


class Enemy(BaseModel):
    name: str
    specialname: str
    enemytype: str
    category: str
    description: str
    rewardpreview: List[RewardpreviewItem]
