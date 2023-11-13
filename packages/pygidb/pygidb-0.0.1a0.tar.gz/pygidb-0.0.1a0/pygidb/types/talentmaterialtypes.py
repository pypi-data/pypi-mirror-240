from typing import List

from pydantic import BaseModel, Field


class TalentMaterialType(BaseModel):
    name: str
    field_2starname: str = Field(..., alias='2starname')
    field_3starname: str = Field(..., alias='3starname')
    field_4starname: str = Field(..., alias='4starname')
    day: List[str]
    location: str
    region: str
    domainofmastery: str
