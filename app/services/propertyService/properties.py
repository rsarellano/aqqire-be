from models.properties.properties import Properties
from sqlalchemy.orm import Session


def get_all_properties(db: Session ):
    return db.query(Property).all()


# def create_property