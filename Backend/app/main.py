from fastapi import FastAPI, Depends

from app.api.routs.auth import router as auth_router
from app.api.dependencies import get_current_user
from app.models.user import User

app = FastAPI()

@app.get("/ping")
def ping():
    return{"msg":"ok"}

@app.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email}

app.include_router(auth_router, prefix="/auth", tags=["auth"])