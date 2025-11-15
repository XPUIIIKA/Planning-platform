from fastapi import APIRouter, Depends

from app.api.dependencies import getCurrentUser
from app.DTOs.user import UserOut
from app.models.user import User


router = APIRouter()

@router.get("/me", response_model=UserOut)
def readCurrentUser(currentUser: User  = Depends(getCurrentUser)) -> UserOut:
    answer = UserOut(
        name=currentUser.userName,
        email=currentUser.email,
        createdAt=currentUser.createdAt
    )
    
    return answer
