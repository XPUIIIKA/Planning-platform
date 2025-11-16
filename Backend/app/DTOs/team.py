from pydantic import BaseModel
from datetime import datetime


class TeamShortOut(BaseModel):
    id: int
    name: str

class TeamOut(BaseModel):
    id: int
    name: str
    createdAt: datetime