from pydantic import BaseModel, EmailStr, str
from datetime import datetime


class TeamShortOut(BaseModel):
    id: int
    name: str