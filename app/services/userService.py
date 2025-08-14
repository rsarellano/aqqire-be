from app.models.users import Users
from sqlalchemy.orm import Session
<<<<<<< HEAD
from app.schemas.user.userSchema import UserBase,UserCreate,UserLogin
from app.utils.jwt_handler import create_access_token

import bcrypt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import HTTPException




def get_all_users(db:Session):
    return db.query(User).all()


def create_user(db:Session, data: UserBase):
    new_user = User()

def get_user_by_email(db: Session, email:str):
    return db.query(Users).filter(Users.user_email == email).first()


def user_login(db: Session,data:UserLogin ):
    user = get_user_by_email(db,data.user_email)
    if not user or not bcrypt.checkpw(data.user_passwrd.encode("utf-8"), user.user_passwrd.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid credentials")


    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

def register_user(db: Session, data: UserCreate):
    existing_user = get_user_by_email(db,data.user_email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = bcrypt.hashpw(data.user_passwrd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    new_user = Users(
        user_email = data.user_email,
        user_firstName = data.user_firstName,
        user_lastName = data.user_lastName,
        user_passwrd =hashed_pw
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
=======
from app.schemas.userSchema import UserBase

def get_all_users(db:Session):
    return db.query(Property).all()


def create_user(db:Session, data: UserBase):
    new_user = User()
>>>>>>> 4e21ccd0929ee65cc1a8d85b91719599453d8b06
