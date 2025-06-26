from app.models.properties import Property
from sqlalchemy.orm import Session
from app.schemas.propertySchema import PropertyBase
from typing import List
from sqlalchemy import or_


def get_all_properties(db: Session ):
    return db.query(Property).all()


def create_property (db:Session, data: PropertyBase ):
    new_property = Property(**data.model_dump())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

def create_properties(db: Session, data: List[PropertyBase] ):
    new_properties = [Property(**prop.model_dump())for prop in data]
    db.add_all(new_properties)
    db.commit()
    for prop in new_properties:
        db.refresh(prop)
    return new_properties


def search_property(db: Session, q: str | None , page: int, items: int):
    searched_property = db.query(Property)

    if q:
        searched_property = searched_property.filter(
            or_( 
                Property.name.ilike(f"%{q}%"),
                Property.address.ilike(f"%{q}%"),
                Property.state.ilike(f"%{q}%"),
                Property.city.ilike(f"%{q}")
            )
        )
    total = searched_property.count()
    results = search_property.offset((page - 1 ) * items).limit(items).all()

    return result, total