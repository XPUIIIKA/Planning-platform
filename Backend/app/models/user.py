from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index = True)
    userName = Column(String, unique = True, index = True, nullable=False)
    hashedPassword = Column(String, nullable=False)
    email = Column(String, unique = True, index = True, nullable=False)
    createdAt = Column(DateTime, server_default=func.now())