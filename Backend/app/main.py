from fastapi import FastAPI, Depends

from app.api.routs.auth import router as auth_router
from app.api.routs.member import router as member_router
from app.api.routs.task import router as task_router
from app.api.routs.team import router as team_router
from app.api.routs.user import router as user_router

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
app.include_router(member_router, prefix="/member", tags=["member"])
app.include_router(task_router, prefix="/task", tags=["task"])
app.include_router(team_router, prefix="/team", tags=["team"])
app.include_router(user_router, prefix="/user", tags=["user"])