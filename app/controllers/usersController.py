from fastapi import APIRouter, HTTPException, Depends, status, FastAPI
from typing import Annotated
from sqlalchemy.orm import Session

from app.schemas.user.userSchema import UserBase, UserResponse, UserCreate
from app.services.userService import register_user
from app.connection.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", response_model=UserResponse)
def register(data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db,data)
