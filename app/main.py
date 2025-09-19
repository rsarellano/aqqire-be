from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, status
from app.connection.database import engine,sessionLocal, Base
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from app.schemas.property.propertySchema import PropertyCreate, PropertyResponse
from app.schemas.user.userSchema import UserBase, UserCreate
from app.models.properties import Property
from app.models.users import Users
from app.services.propertyService import get_all_properties, create_property
from app.controllers.propertiesController import router as property_router
from app.controllers.usersController import router as user_router
from fastapi.middleware.cors import CORSMiddleware 
from passlib.context import CryptContext
from app.connection.database import Base, engine
import asyncio


app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(property_router)
app.include_router(user_router)

app.include_router(property_router)

# @app.on_event("startup")
# async def startup_event():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     print("Tables ensured on startup")