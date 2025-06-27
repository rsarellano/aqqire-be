from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, Query
from typing import Annotated, List, Optional
from sqlalchemy.orm import Session


from app.schemas.propertySchema import PropertyResponse, PropertyCreate
from app.services.propertyService import update_property, search_property, get_all_properties, create_property, create_properties


from app.connection.database import get_db


router = APIRouter(
    prefix="/properties",
    tags=["Properties"]
)



db_dependency = Annotated[Session, Depends(get_db)]



# Creating single property
@router.post("/", response_model=PropertyCreate, status_code=status.HTTP_201_CREATED)
def create_new_property(property: PropertyCreate, db: Session = Depends(get_db)):
    return create_property(db,property)
    
#  Create Multiple Properties
@router.post("/bulk", response_model=List[PropertyCreate], status_code=status.HTTP_201_CREATED)
def create_new_properties(properties: List[PropertyCreate], db: Session = Depends(get_db)):
    return create_properties(db,properties)
    
#  Get All Properties
@router.get("/", response_model=list[PropertyCreate])
def list_properties(db: db_dependency):
    return get_all_properties(db)

# Search for properties
@router.post("/search/")
def search_properties(q: str = Query(default=None) ,page: int = Query(default=1,ge=1),items: int = Query(default=10, ge=1), db: Session = Depends(get_db)):
    results, total = search_property(db,q,page,items)

    return {
        "data": [PropertyResponse.from_orm(r) for r in results],
        "total": total,
        "page": page,
        "items": items
    }


@router.put("/{property_id}", response_model=PropertyResponse)
def update_exisiting_property(
    property_id: int,
    property_data: PropertyCreate,
    db: Session = Depends(get_db)
):

    updated = update_property(db, property_id, property_data)
    if not updated:
         raise HTTPException(status_code=404, detail="Property not found")
    return updated