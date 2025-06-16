from app.models.users import Users
from sqlalchemy.orm import Session
from app.schemas.userSchema import UserBase

def get_all_users(db:Session):
    return db.query(Property).all()


def create_user(db:Session, data: UserBase):
    new_user = User()