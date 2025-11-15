from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi import HTTPException

from app.config import settings


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
REFRESH_TOKEN_LIFETIME_DAYS = settings.refresh_token_lifetime_days

def createAccessToken(subject: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    toEncode = {"sub": str(subject), "exp": expire}
    encodedJwt = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodedJwt

def createRefreshToken(subject: str):
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_LIFETIME_DAYS)
    toEncode = {"sub": str(subject), "exp": expire, "type": "refresh"}
    encodedJwt = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodedJwt

def decodeToken(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail=f"invalid token {str(e)}")