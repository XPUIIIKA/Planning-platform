from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.user import User
from app.models.team import Team


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, default="new")
    priority: Mapped[str] = mapped_column(String, default="medium")

    ownerId: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assignedId: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    teamId: Mapped[Optional[int]] = mapped_column(ForeignKey("teams.id"), nullable=True)

    createdAt: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updatedAt: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    owner: Mapped[User] = relationship("User", foreign_keys=[ownerId])
    assigned: Mapped[Optional[User]] = relationship("User", foreign_keys=[assignedId])
    team: Mapped[Optional[Team]] = relationship("Team", foreign_keys=[teamId])