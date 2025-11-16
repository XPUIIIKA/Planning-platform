from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.user import User
from app.models.team import Team


class TeamMember(Base):
    __tablename__ = "team_members"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    teamId: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    joinedAt: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'member')", name="role_check"),
    )

    user: Mapped[User] = relationship("User", foreign_keys=[userId])
    team: Mapped[Team] = relationship("Team", foreign_keys=[teamId])
