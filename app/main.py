from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, status
from app.connection.database import engine,sessionLocal, Base
from sqlalchemy.orm import Session

from app.schemas.propertySchema import PropertyCreate, PropertyBase
from app.models.properties import Property
from app.services.propertyService import get_all_properties, create_property
from app.controllers.properties import router as property_router


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(property_router)

