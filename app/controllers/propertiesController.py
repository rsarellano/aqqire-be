from fastapi import APIRouter, HTTPException, Depends, status, FastAPI, Query
from typing import Annotated, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.property.propertySchemaAI import SearchPrompt
from app.schemas.property.propertySchema import PropertyResponse, PropertyCreate
from app.services.propertyService import update_property, search_property, get_all_properties, create_property, create_properties, search_properties_with_ai
from app.utils.jwt_handler import get_current_user
from app.models.properties import Property
from app.models.users import Users
from fastapi.security import OAuth2PasswordBearer
from app.connection.database import get_db



router = APIRouter(
    prefix="/properties",
    tags=["Properties"]
)



db_dependency = Annotated[Session, Depends(get_db)]



# Creating single property
@router.post("/", response_model=PropertyCreate, status_code=status.HTTP_201_CREATED)
async def create_new_property(property: PropertyCreate, db: AsyncSession = Depends(get_db),
current_user: Users = Depends(get_current_user)):
    return await create_property(db,property, current_user)
    
#  Create Multiple Properties
@router.post("/bulk", response_model=List[PropertyCreate], status_code=status.HTTP_201_CREATED)
def create_new_properties(properties: List[PropertyCreate], db: Session = Depends(get_db)):
    return create_properties(db,properties)
    
#  Get All Properties
@router.get("/", response_model=list[PropertyCreate])
async def list_properties(db: db_dependency):
    return await get_all_properties(db)

# @router.post("/sel_properties(db)


# Search for properties/")
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




# @router.patch("/properties/{property_id}/status")
# def set_property_status(
#     property_id: int,
#     status_update: PropertyCreate,
#     db: Session = Depends(get_db)
# ):
#     updated = update_property_status(db, property_id, status_update.status)
#     if not updated:
#         raise HTTPException(status_code=404, detail="Property not found")
#     return updated




# AI search

# @router.post("/search-ai")
# def search_ai_with_gpt(request: SearchPrompt, db: Session = Depends(get_db)):
#     matching_ids = search_properties_with_ai(request.prompt, db)

#     result = db.query(Property).filter(Property.id.in_(matching_ids)).all()
#     return {"ids": matching_ids}



@router.post("/search-ai")
def search_ai_with_gpt(request: SearchPrompt, db: Session = Depends(get_db)):
    matching_ids = search_properties_with_ai(request.prompt, db)

    if not matching_ids:
        return {"properties": []}

    # Query full property data
    results = db.query(Property).filter(Property.id.in_(matching_ids)).all()

    # Return as JSON (manually or using a response model)
    property_data = [
        {
            "id": p.id,
            "name": p.name,
            "city": p.city,
            "state": p.state,
            "address": p.address,
            "price": p.price,
        }
        for p in results
    ]

    return {"properties": property_data}
