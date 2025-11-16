from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.services.memberService import MemberService
from app.DTOs.member import MemberShortOut
from app.models.user import User
from app.api.dependencies import getCurrentUser, getDb

router = APIRouter()


@router.get("/{teamId}/members", response_model=List[MemberShortOut])
def getTeamMembers(teamId: int, currentUser: User = Depends(getCurrentUser), db: Session = Depends(getDb)):
    service = MemberService(db)
    return service.getMembersForTeam(currentUser.id, teamId)

@router.post("/{teamId}/members/{userId}", response_model=MemberShortOut)
def addMember(teamId: int, userId: int, currentUser: User = Depends(getCurrentUser), db: Session = Depends(getDb)):
    service = MemberService(db)
    return service.addMember(ownerId=currentUser.id, userId=userId, teamId=teamId)

@router.delete("/members/{memberId}", status_code=204)
def deleteMember(memberId: int, currentUser: User = Depends(getCurrentUser), db: Session = Depends(getDb)):
    service = MemberService(db)
    service.deleteMember(ownerId=currentUser.id, memberId=memberId)
    return None

@router.post("/{teamId}/leave", status_code=204)
def leaveTeam(teamId: int, currentUser: User = Depends(getCurrentUser), db: Session = Depends(getDb)):
    service = MemberService(db)
    service.leaveTeam(userId=currentUser.id, teamId=teamId)
    return None
