from pydantic import BaseModel


class Element(BaseModel):
    name: str
    type: str
    color: str
    region: str
    archon: str
    theme: str
