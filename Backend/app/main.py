from fastapi import FastAPI, Depends

from app.api.routs.auth import router as auth_router
from app.api.dependencies import getCurrentUser
from app.models.user import User

app = FastAPI()

@app.get("/ping")
def ping():
    return{"msg":"ok"}

@app.get("/me")
def me(currentUser: User = Depends(getCurrentUser)):
    return {"id": currentUser.id, "email": currentUser.email}

app.include_router(auth_router, prefix="/auth", tags=["auth"])