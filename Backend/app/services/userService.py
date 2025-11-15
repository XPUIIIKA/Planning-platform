from sqlalchemy.orm import Session

from app.models.user import User
from app.DTOs.user import UserCreate
from app.services.hashService import hashPassword

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def foundUserByEmail(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
    
    def registerUser(self, userData: UserCreate) -> User:
        user = User(
            name=userData.name, 
            email=userData.email, 
            hashedPassword=hashPassword(userData.password)
            )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user