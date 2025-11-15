from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException

from app.DTOs.team import TeamShortOut
from app.models.team import Team
from app.models.teamMember import TeamMember


class TeamService:
    def __init__(self, db: Session):
        self.db = db

    def getTeamsForUser(self, userId: int) -> List[TeamShortOut] :
        teamMembers = (
            self.db.query(TeamMember)
            .join(Team, Team.id == TeamMember.teamId)
            .filter(TeamMember.userId == userId)
            .all()
        )

        if not teams:
            return []

        teams:List[Team] = [teamMember.team for teamMember in teamMembers]

        return [TeamShortOut(id=team.id, name=team.name) for team in teams]
    
    def leaveTeam(self, userId: int, teamId: int) -> bool:
        team_member = (
            self.db.query(TeamMember)
            .filter(TeamMember.userId == userId, TeamMember.teamId == teamId)
            .first()
        )

        if not team_member:
            raise HTTPException(status_code=404, detail=f"User {userId} is not a member of team {teamId}")

        self.db.delete(team_member)
        self.db.commit()
        return True