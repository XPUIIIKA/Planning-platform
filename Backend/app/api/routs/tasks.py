from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.DTOs.task import TaskOut, TaskCreate
from app.api.dependencies import get_db, get_current_user
from app.models.task import Task

router = APIRouter()

@router.post("/", response_model = TaskOut)
def create_task(data: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = Task(
        title = data.title,
        description = data.description,
        priority = data.priority,
        owner_id = current_user.id,
        assigned_id = data.assigned_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/", response_model = list[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    db.query(Task)