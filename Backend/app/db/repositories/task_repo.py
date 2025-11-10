from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.task import Task


class TaskRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_task(self, task: Task):
        self.db.add(task)
        await self.db.commit()
        await self.db.refresh(task)
        return task

    async def get_by_id(self, task_id: int):
        result = await self.db.execute(
            select(Task).where(Task.id == task_id)
        )
        return result.scalar_one_or_none()

    async def get_tasks_by_team(self, team_id: int):
        result = await self.db.execute(
            select(Task).where(Task.team_id == team_id)
        )
        return result.scalars().all()

    async def get_tasks_by_owner(self, owner_id: int):
        result = await self.db.execute(
            select(Task).where(Task.owner_id == owner_id)
        )
        return result.scalars().all()

    async def get_tasks_by_assigned(self, user_id: int):
        result = await self.db.execute(
            select(Task).where(Task.assigned_id == user_id)
        )
        return result.scalars().all()

    async def list_all(self):
        result = await self.db.execute(select(Task))
        return result.scalars().all()

    async def update_task(self, task: Task, data: dict):
        for key, value in data.items():
            setattr(task, key, value)
        await self.db.commit()
        await self.db.refresh(task)
        return task

    async def delete_task(self, task: Task):
        await self.db.delete(task)
        await self.db.commit()
