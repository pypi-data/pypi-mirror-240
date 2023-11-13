from typing import Optional

from pydantic import BaseModel


class GroupReward(BaseModel):
    name: str


class AchievementGroups(BaseModel):
    name: str
    sortorder: int
    reward: GroupReward


# Achievement
class StageReward(BaseModel):
    name: str
    count: int


class Stage(BaseModel):
    title: str
    description: str
    progress: int
    reward: StageReward


class Achievement(BaseModel):
    name: str
    achievementgroup: str
    sortorder: int
    stages: int
    stage1: Stage
    stage2: Optional[Stage]
    stage3: Optional[Stage]
