from models.properties.properties import Property
from sqlalchemy.orm import Session
from schemas.propertySchema import PropertyBase


def get_all_properties(db: Session ):
    return db.query(Property).all()


def create_property (db:Session, data: PropertyBase ):
    new_property = Property