from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, status
from app.connection.database import engine,sessionLocal, Base

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
from fastapi.security import OAuth2PasswordBearer
import asyncio
from fastapi.openapi.utils import get_openapi

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Aqqire API",
        version="1.0.0",
        description="Property management API",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.middleware("http")
async def log_headers(request, call_next):
    print("AUTH HEADER RECEIVED:", request.headers.get("authorization"))
    response = await call_next(request)
    return response



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],
     allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(property_router)
app.include_router(user_router)

app.include_router(property_router)

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables ensured on startup")