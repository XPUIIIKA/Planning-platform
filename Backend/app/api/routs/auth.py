from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.api.DTOs.user import UserCreate
from app.api.DTOs.token import RefreshTokenRequest
from app.services.tokens import create_access_token, create_refresh_token, decode_token
from app.api.dependencies import get_db

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"])


@router.post("/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="email already exists")
    
    hashed = pwd_context.hash(user_data.password)
    user = User(email=user_data.email, hashed_password=hashed, user_name=user_data.name)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"id": user.id, "user_name": user.user_name}

@router.post("/login")
def login(user_date: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_date.email).first()
    if not user or not pwd_context.verify(user_date.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="invalid credentials")
    
    acToken = create_access_token(user.id)
    reToken = create_refresh_token(user.id)
    
    return {"access_token": acToken, "refresh_token": reToken}
    
@router.post("/refresh")
def refresh(dto: RefreshTokenRequest):
    data = decode_token(dto.refresh_token)
    if data.get("type") != "refresh":
        raise HTTPException(status_code=400, detail="invalid token type")
    
    new_access = create_access_token(data["sub"])
    
    return {"access_token": new_access}