from typing import List

from pydantic import BaseModel


class NameCard(BaseModel):
    name: str
    description: str
    sortorder: int
    source: List[str]
