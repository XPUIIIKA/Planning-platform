from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"
    assigned_id: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_id: Optional[str] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    owner_id: int
    assigned_id: int

    class Config:
        orm_mode: True