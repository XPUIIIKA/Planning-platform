from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"
    assignedId: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assignedId: Optional[str] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    ownerId: int
    assignedId: int

    class Config:
        orm_mode: True