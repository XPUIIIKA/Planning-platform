from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="new")
    priority = Column(String, default="medium")

    ownerId = Column(Integer, ForeignKey("users.id"))
    assignedId = Column(Integer, ForeignKey("users.id"), nullable=True)
    teamId = Column(Integer, ForeignKey("teams.id"), nullable=True)

    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    owner = relationship("User", foreign_keys=[ownerId])
    assigned = relationship("User", foreign_keys=[assignedId])
    team = relationship("Team", foreign_keys=[teamId])