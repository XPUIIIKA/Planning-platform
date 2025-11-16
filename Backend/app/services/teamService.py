from sqlalchemy.orm import Session
from typing import List

from app.DTOs.team import TeamShortOut, TeamOut
from app.models.team import Team
from app.models.task import Task
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

    def createTeam(self, name: str, userId: int) -> TeamOut:
        new_team = Team(name=name)
        self.db.add(new_team)
        self.db.commit()
        self.db.refresh(new_team)

        team_member = TeamMember(userId=userId, teamId=new_team.id, role='admin')
        self.db.add(team_member)
        self.db.commit()

        return TeamOut(id=new_team.id, name=new_team.name, createdAt=new_team.createdAt)
    
    def isUserInTeam(self, teamId: int, userId: int) -> bool:
        membership = (
            self.db.query(TeamMember)
            .filter(TeamMember.teamId == teamId, TeamMember.userId == userId)
            .first()
        )
        return membership is not None
    
    def canUserUpdateTask(self, userId: int, taskId: int) -> bool:
        task = self.db.query(Task).filter(Task.id == taskId).first()

        if task.ownerId == userId:
            return True

        if task.teamId:
            membership = (
                self.db.query(TeamMember)
                .filter(TeamMember.team_id == task.teamId, TeamMember.userId == userId)
                .first()
            )
            if membership and membership.role == "admin":
                return True

        return False

    def getTeamIdByTask(self, taskId: int) -> int | None:
        task = self.db.query(Task).filter(Task.id == taskId).first()
        if task:
            return task.teamId
        return None