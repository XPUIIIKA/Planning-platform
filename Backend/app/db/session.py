from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engin = create_engine(settings.database_url , connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind = engin, autocommit = False, autoflush = False)