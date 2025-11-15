from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.tokens import decodeToken
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getCurrentUser(token: str = Depends(oauth2_scheme), db: Session = Depends(getDb)) -> User:
    data = decodeToken(token)
    userId = data.get("sub")

    if not userId:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.query(User).filter(User.id == int(userId)).first()

    if not user:
        raise HTTPException(status_code=401, detail="user not found")
    
    return user

