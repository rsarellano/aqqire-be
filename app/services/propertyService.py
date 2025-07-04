from app.models.properties import Property
from sqlalchemy.orm import Session
from app.schemas.propertySchema import PropertyCreate
from typing import List
from sqlalchemy import or_


def get_all_properties(db: Session ):
    return db.query(Property).all()


def create_property (db:Session, data: PropertyCreate ):
    new_property = Property(**data.model_dump())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

def create_properties(db: Session, data: List[PropertyCreate] ):
    new_properties = [Property(**prop.model_dump())for prop in data]
    db.add_all(new_properties)
    db.commit()
    for prop in new_properties:
        db.refresh(prop)
    return new_properties


def update_property(db: Session,property_id: int , data: PropertyCreate):
    updated_property = db.query(Property).filter(Property.id == property_id).first()
    if not updated_property:
        return None

    for field, value in data.model_dump().items():
        setattr(updated_property, field, value)

    db.commit()
    db.refresh(updated_property)
    return updated_property

def search_property(db: Session, q: str | None , page: int, items: int):
    query_property = db.query(Property)

    if q:
        query_property = query_property.filter(
            or_( 
                Property.name.ilike(f"%{q}%"),
                Property.address.ilike(f"%{q}%"),
                Property.state.ilike(f"%{q}%"),
                Property.city.ilike(f"%{q}")
            )
        )
    total = query_property.count()
    results = query_property.offset((page - 1 ) * items).limit(items).all()

    return results, total