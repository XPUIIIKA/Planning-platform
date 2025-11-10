from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.team import Team
from app.models.team_member import TeamMember


class TeamRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_team(self, team: Team):
        self.db.add(team)
        await self.db.commit()
        await self.db.refresh(team)
        return team

    async def get_by_id(self, team_id: int):
        result = await self.db.execute(
            select(Team).where(Team.id == team_id)
        )
        return result.scalar_one_or_none()

    async def get_user_teams(self, user_id: int):
        result = await self.db.execute(
            select(Team)
            .join(TeamMember, TeamMember.team_id == Team.id)
            .where(TeamMember.user_id == user_id)
        )
        return result.scalars().all()

    async def add_member(self, member: TeamMember):
        self.db.add(member)
        await self.db.commit()
        await self.db.refresh(member)
        return member

    async def get_member(self, user_id: int, team_id: int):
        result = await self.db.execute(
            select(TeamMember)
            .where(
                TeamMember.user_id == user_id,
                TeamMember.team_id == team_id
            )
        )
        return result.scalar_one_or_none()

    async def get_team_members(self, team_id: int):
        result = await self.db.execute(
            select(TeamMember)
            .where(TeamMember.team_id == team_id)
        )
        return result.scalars().all()

    async def remove_member(self, member: TeamMember):
        await self.db.delete(member)
        await self.db.commit()

    async def delete_team(self, team: Team):
        await self.db.delete(team)
        await self.db.commit()
