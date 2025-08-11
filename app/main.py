from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, status
from app.connection.database import engine,sessionLocal, Base
from sqlalchemy.orm import Session

from app.schemas.property.propertySchema import PropertyCreate, PropertyResponse
from app.models.properties import Property
from app.services.propertyService import get_all_properties, create_property
from app.controllers.propertiesController import router as property_router
from fastapi.middleware.cors import CORSMiddleware 

Base.metadata.create_all(bind=engine)



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(property_router)

