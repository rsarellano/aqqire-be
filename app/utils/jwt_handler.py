import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
import os
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.connection.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

secret_key = os.getenv("SECRET_KEY")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

SECRET_KEY = secret_key
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
   
    if "sub" not in to_encode:
        to_encode["sub"] = str(data.get("id") or data.get("user_id"))
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    print("TOKEN RECEIVED:", token) 
    payload = verify_access_token(token)
    user_id: str = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = await db.get(Users, int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user