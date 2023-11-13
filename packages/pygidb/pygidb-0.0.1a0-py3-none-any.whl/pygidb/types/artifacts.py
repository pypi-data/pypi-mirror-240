from typing import List

from pydantic import BaseModel, Field


class Piece(BaseModel):
    name: str
    relictype: str
    description: str
    story: str


class Artifact(BaseModel):
    name: str
    rarity: List[str]
    field_2pc: str = Field(..., alias='2pc')
    field_4pc: str = Field(..., alias='4pc')
    flower: Piece
    plume: Piece
    sands: Piece
    goblet: Piece
    circlet: Piece
