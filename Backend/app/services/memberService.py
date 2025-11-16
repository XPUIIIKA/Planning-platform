from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException

from app.models.teamMember import TeamMember
from app.models.team import Team
from app.DTOs.member import MemberShortOut


class MemberService:
    def __init__(self, db: Session):
        self.db = db

    def _checkOwner(self, userId: int, teamId: int):
        team = self.db.query(Team).filter(Team.id == teamId).first()
        if not team:
            raise HTTPException(status_code=404, detail=f"Team {teamId} not found")
        if team.ownerId != userId:
            raise HTTPException(status_code=403, detail="Only team owner can perform this action")

    def leaveTeam(self, userId: int, teamId: int):
        teamMember = (
            self.db.query(TeamMember)
            .filter(TeamMember.userId == userId, TeamMember.teamId == teamId)
            .first()
        )

        if not teamMember:
            raise HTTPException(status_code=404, detail=f"User {userId} is not a member of team {teamId}")

        self.db.delete(teamMember)
        self.db.commit()
    
    def getMembersForTeam(self, userId: int, teamId: int) -> list[MemberShortOut]:
        self._checkOwner(userId, teamId)

        members = (
            self.db.query(TeamMember)
            .options(joinedload(TeamMember.user))
            .filter(TeamMember.teamId == teamId)
            .all()
        )
        
        return [MemberShortOut(id=member.id, name=member.user.name, role=member.role) for member in members]
    
    def addMember(self, ownerId: int, userId: int, teamId: int) -> MemberShortOut:
        self._checkOwner(ownerId, teamId)

        existingMember = (
            self.db.query(TeamMember)
            .filter(TeamMember.userId == userId, TeamMember.teamId == teamId)
            .first()
        )

        if existingMember:
            raise HTTPException(status_code=400, detail=f"User {userId} is already a member of team {teamId}")

        newMember = TeamMember(userId=userId, teamId=teamId, role="member")
        self.db.add(newMember)
        self.db.commit()
        self.db.refresh(newMember)

        return MemberShortOut(id=newMember.id, name=newMember.user.name, role=newMember.role)
    
    def deleteMember(self, ownerId: int, memberId: int):
        member = self.db.query(TeamMember).filter(TeamMember.id == memberId).first()

        if not member:
            raise HTTPException(status_code=404, detail=f"Member with id {memberId} not found")

        self._checkOwner(ownerId, member.teamId)

        self.db.delete(member)
        self.db.commit()
