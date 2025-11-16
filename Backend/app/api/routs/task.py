from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import getDb, getCurrentUser
from app.services.taskService import TaskService
from app.services.teamService import TeamService
from app.DTOs.task import TaskCreate, TaskUpdate, TaskOut
from app.models.user import User


router = APIRouter()


@router.get("/{taskId}/tasks", response_model=List[TaskOut])
def getTasksForTeam(teamId: int, db: Session = Depends(getDb), currentUser: User  = Depends(getCurrentUser)):
    taskService = TaskService(db)
    teamService = TeamService(db)
    
    if not teamService.isUserInTeam(teamId=teamId, userId=currentUser.id):
        raise HTTPException(status_code=403, detail="Not authorized to access this team's tasks")

    return taskService.getTasksForTeam(teamId)

@router.post("/{taskId}/tasks", response_model=TaskOut)
def addTaskForTeam(teamId: int, data: TaskCreate, db: Session = Depends(getDb), currentUser: User  = Depends(getCurrentUser)):
    taskService = TaskService(db)
    teamService = TeamService(db)
    
    if not teamService.isUserInTeam(teamId=teamId, userId=currentUser.id):
        raise HTTPException(status_code=403, detail="Not authorized to access this team's tasks")
    
    return taskService.addTask(teamId=teamId, ownerId=currentUser.id, data=data)

@router.put("/tasks/{taskId}", response_model=TaskOut)
def updateTask(taskId: int, data: TaskUpdate, db: Session = Depends(getDb), currentUser: User  = Depends(getCurrentUser)):
    taskService = TaskService(db)
    teamService = TeamService(db)
    
    teamId = teamService.getTeamIdByTask(taskId)

    if not teamService.isUserInTeam(teamId=teamId, userId=currentUser.id):
        raise HTTPException(status_code=403, detail="Not authorized to access this team's tasks")
    
    if not teamService.canUserUpdateTask(currentUser.id, taskId):
        raise HTTPException(status_code=403, detail="Not authorized to access this team's tasks")

    return taskService.updateTask(taskId=taskId, data=data)

@router.delete("/tasks/{taskId}", status_code=204)
def deleteTask(taskId: int, db: Session = Depends(getDb), currentUser: User  = Depends(getCurrentUser)):
    taskService = TaskService(db)
    teamService = TeamService(db)
    
    teamId = teamService.getTeamIdByTask(taskId)

    if not teamService.isUserInTeam(teamId=teamId, userId=currentUser.id):
        raise HTTPException(status_code=403, detail="Not authorized to access this team's tasks")
    
    if not teamService.canUserUpdateTask(currentUser.id, taskId):
        raise HTTPException(status_code=403, detail="Not authorized to access this team's tasks")
    
    taskService.deleteTask(taskId=taskId)
    return None
