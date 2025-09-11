from fastapi import APIRouter, HTTPException, Depends, status, FastAPI
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user.userSchema import UserBase, UserResponse, UserCreate, UserLogin
from app.services.userService import register_user, user_login
from app.connection.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", response_model=UserResponse)
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(db,data)



@router.post("/login")
async def login(data: UserLogin, db: AsyncSession = Depends(get_db)):
    return await user_login(db,data)
