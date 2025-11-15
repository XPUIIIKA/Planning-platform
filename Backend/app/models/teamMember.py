from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    teamId = Column(Integer, ForeignKey("teams.id"), nullable=False)
    role = Column(String, nullable=False)
    joinedAt = Column(DateTime, server_default=func.now())

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'member')", name="role_check"),
    )

    user = relationship("User", foreign_keys=[userId])
    team = relationship("Team", foreign_keys=[teamId])