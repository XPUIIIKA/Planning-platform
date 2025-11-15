from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.DTOs.user import UserCreate
from app.DTOs.token import RefreshTokenRequest
from app.api.dependencies import getDb
from app.services.tokens import createAccessToken, createRefreshToken, decodeToken
from app.services.hashService import verifyPassword
from app.services.userService import UserService

router = APIRouter()

@router.post("/register")
def register(userData: UserCreate, db: Session = Depends(getDb)):
    userService = UserService(db)

    existing = userService.foundUserByEmail(userData.email)

    if existing:
        raise HTTPException(status_code=400, detail="email already exists")
    
    user = userService.registerUser(userData)

    return {"id": user.id, "user_name": user.userName}

@router.post("/login")
def login(userData: UserCreate, db: Session = Depends(getDb)):
    userService = UserService(db)

    user = userService.foundUserByEmail(userData.email)

    if not user or not verifyPassword(userData.password, user.hashedPassword):
        raise HTTPException(status_code=400, detail="invalid credentials")
    
    acToken = createAccessToken(user.id)
    reToken = createRefreshToken(user.id)
    
    return {"access_token": acToken, "refresh_token": reToken}
    
@router.post("/refresh")
def refresh(dto: RefreshTokenRequest):
    data = decodeToken(dto.refreshToken)
    if data.get("type") != "refresh":
        raise HTTPException(status_code=400, detail="invalid token type")
    
    newAccess = createAccessToken(data["sub"])
    
    return {"access_token": newAccess}