from pydantic import BaseModel


class Geography(BaseModel):
    name: str
    area: str
    description: str
    region: str
    showonlyunlocked: bool = False
    sortorder: int
