from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.api.dependencies import getDb, getCurrentUser
from app.DTOs.team import TeamShortOut
from app.models.user import User
from app.services.teamService import TeamService


router = APIRouter()

@router.get("/myTeams", response_model=List[TeamShortOut])
def getMyTeams(currentUser: User  = Depends(getCurrentUser), db: Session = Depends(getDb)) -> List[TeamShortOut]:
    service = TeamService(db)
    return  service.getTeamsForUser(currentUser.id)

@router.post("/leaveTeam", response_model=List[TeamShortOut])
def leaveTeam(teamId: int, currentUser: User  = Depends(getCurrentUser), db: Session = Depends(getDb)) -> bool:
    service = TeamService(db)
    return service.leaveTeam(currentUser.id, teamId)
    