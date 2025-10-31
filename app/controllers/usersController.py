from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, Response, Request
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user.userSchema import UserBase, UserResponse, UserCreate, UserLogin
from app.services.userService import register_user, user_login
from app.connection.database import get_db
from app.utils.jwt_handler import verify_access_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", response_model=UserResponse)
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(db,data)



@router.post("/login")
async def login(data: UserLogin,
                response: Response,
                db: AsyncSession = Depends(get_db)):
    
    token = await user_login(db,data)
    
    response.set_cookie(
    key="access_token",
    value=token["access_token"],
    httponly=True,
    samesite="None",     
    secure=True,       
    max_age=3600
    # domain = "None"
)
    
    
    return {"message": "Login successful"}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        httponly=True,
        samesite="lax",
        secure=False
    )
    return {"message": "Logout successful"}


# @router.get("/auth/me")
# async def get_current_user(request: Request):
#     token = request.cookies.get("access_token")
#     print("TOKEN VALUE:", token)
#     if not token:
#         return {"authenticated": False}
    
#     try:
#         payload = verify_access_token(token)
#         return{"authenticated" : True, "user_id": payload["sub"]}
#     except:
#         return{"authenticated": False}
    
@router.get("/auth/me")
async def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    print("COOKIE RECEIVED:", token)

    if not token:
        print("No token found in cookies")
        return {"authenticated": False}

    try:
        print("Verifying token...")
        payload = verify_access_token(token)
        print("TOKEN PAYLOAD:", payload)
        return {"authenticated": True, "user_id": payload["sub"]}
    except Exception as e:
        print("TOKEN VERIFICATION FAILED:", e)
        return {"authenticated": False}

