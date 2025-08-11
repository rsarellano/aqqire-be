from app.models.users import Users
from sqlalchemy.orm import Session
from app.schemas.userSchema import UserBase
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

def get_all_users(db:Session):
    return db.query(User).all()


def create_user(db:Session, data: UserBase):
    new_user = User()


def register_user()