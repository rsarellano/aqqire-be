from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, status
from app.connection.database import engine,sessionLocal, Base
<<<<<<< HEAD
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
=======
from sqlalchemy.orm import Session

from app.schemas.propertySchema import PropertyCreate, PropertyResponse
from app.models.properties import Property
from app.services.propertyService import get_all_properties, create_property
from app.controllers.propertiesController import router as property_router
from fastapi.middleware.cors import CORSMiddleware 
>>>>>>> 4e21ccd0929ee65cc1a8d85b91719599453d8b06

Base.metadata.create_all(bind=engine)



app = FastAPI()

<<<<<<< HEAD
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
=======
>>>>>>> 4e21ccd0929ee65cc1a8d85b91719599453d8b06

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
<<<<<<< HEAD

app.include_router(property_router)
app.include_router(user_router)
=======
>>>>>>> 4e21ccd0929ee65cc1a8d85b91719599453d8b06

app.include_router(property_router)

<<<<<<< HEAD

=======
>>>>>>> 4e21ccd0929ee65cc1a8d85b91719599453d8b06
