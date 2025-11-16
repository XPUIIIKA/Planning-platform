from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.task import Task
from app.DTOs.task import TaskCreate, TaskUpdate, TaskOut


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def getTasksForTeam(self, teamId: int) -> list[TaskOut]:
        tasks = (
            self.db.query(Task)
            .filter(Task.teamId == teamId)
            .all()
        )
        return tasks

    def addTask(self, teamId: int, ownerId: int, data: TaskCreate) -> TaskOut:
        task = Task(
            title=data.title,
            description=data.description,
            priority=data.priority,
            ownerId=ownerId,
            assignedId=data.assignedId,
            teamId=teamId
        )

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return TaskOut(
            id = task.id,
            title = task.title,
            description = task.description,
            status = task.status,
            priority = task.priority,
            ownerId = task.ownerId,
            assignedId = task.assignedId
            )

    def deleteTask(self, taskId: int):
        task = self.db.query(Task).filter(Task.id == taskId).first()
        if task is None:
            raise HTTPException(status_code=404, detail="task not found")

        self.db.delete(task)
        self.db.commit()

    def updateTask(self, taskId: int, data: TaskUpdate) -> TaskOut:
        task = self.db.query(Task).filter(Task.id == taskId).first()
        if task is None:
            raise HTTPException(status_code=404, detail="task not found")

        if data.title is not None:
            task.title = data.title

        if data.description is not None:
            task.description = data.description

        if data.status is not None:
            task.status = data.status

        if data.priority is not None:
            task.priority = data.priority

        if data.assignedId is not None:
            task.assignedId = data.assignedId

        self.db.commit()
        self.db.refresh(task)

        return TaskOut(
            id = task.id,
            title = task.title,
            description = task.description,
            status = task.status,
            priority = task.priority,
            ownerId = task.ownerId,
            assignedId = task.assignedId
            )
