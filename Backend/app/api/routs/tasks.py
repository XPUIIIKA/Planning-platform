from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.DTOs.task import TaskOut, TaskCreate
from app.api.dependencies import getDb, getCurrentUser
from app.models.task import Task

router = APIRouter()

@router.post("/", response_model = TaskOut)
def createTask(data: TaskCreate, db: Session = Depends(getDb), currentUser = Depends(getCurrentUser)):
    task = Task(
        title = data.title,
        description = data.description,
        priority = data.priority,
        ownerId = currentUser.id,
        assignedId = data.assignedId
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/", response_model = list[TaskOut])
def getTasks(db: Session = Depends(getDb)):
    db.query(Task)