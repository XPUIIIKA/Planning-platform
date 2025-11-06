from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI()

@app.get("/ping")
def ping():
    return{"msg":"ok"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])