from typing import List, Optional

from pydantic import BaseModel


class Outfit(BaseModel):
    name: str
    description: str
    isdefault: bool
    character: str
    source: Optional[List[str]] = None
