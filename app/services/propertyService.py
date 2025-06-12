from app.models.properties import Property
from sqlalchemy.orm import Session
from app.schemas.propertySchema import PropertyBase


def get_all_properties(db: Session ):
    return db.query(Property).all()


def create_property (db:Session, data: PropertyBase ):
    new_property = Property(**data.model_dump())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

