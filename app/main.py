from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends, status
from app.connection.database import engine,sessionLocal, Base
from sqlalchemy.orm import Session

from app.schemas.propertySchema import PropertyCreate, PropertyBase
from app.models.properties import Property
from app.services.propertyService import get_all_properties, create_property

Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()

# db_dependancy = Annotated[Session, Depends(get_db)]



# @app.post("/", response_model=PropertyCreate, status_code=status.HTTP_201_CREATED)
# def create_new_property(property: PropertyBase, db: Session = Depends(get_db)):
#     return create_property(db,property)
    