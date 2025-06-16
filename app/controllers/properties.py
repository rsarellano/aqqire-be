from fastapi import APIRouter, HTTPException, Depends, status, FastAPI
from typing import Annotated
from sqlalchemy.orm import Session


from app.schemas.propertySchema import PropertyBase, PropertyCreate
from app.services.propertyService import get_all_properties, create_property


from app.connection.database import get_db


router = APIRouter(
    prefix="/properties",
    tags=["Properties"]
)



db_dependency = Annotated[Session, Depends(get_db)]




@router.post("/", response_model=PropertyCreate, status_code=status.HTTP_201_CREATED)
def create_new_property(property: PropertyBase, db: Session = Depends(get_db)):
    return create_property(db,property)
    

@router.get("/", response_model=list[PropertyCreate])
def list_properties(db: db_dependency):
    return get_all_properties(db)