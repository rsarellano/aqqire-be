from app.models.users import Users
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.user.userSchema import UserBase,UserCreate,UserLogin
from app.utils.jwt_handler import create_access_token
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import HTTPException




def get_all_users(db:Session):
    return db.query(User).all()


async def create_user(db:AsyncSession, data: UserBase):
    new_user = User()

# async def get_user_by_email(db: AsyncSession, email:str):
#     return await db.query(Users).filter(Users.user_email == email).first()
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(
        select(Users).where(Users.user_email == email)
    )
    return result.scalars().first()

async def user_login(db: AsyncSession,data:UserLogin ):
    user = await get_user_by_email(db,data.user_email)
    if not user or not bcrypt.checkpw(data.user_passwrd.encode("utf-8"),
     user.user_passwrd.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid credentials")


    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

async def register_user(db: AsyncSession, data: UserCreate):
    existing_user = await get_user_by_email(db,data.user_email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = bcrypt.hashpw(data.user_passwrd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    new_user = Users(
        user_email = data.user_email,
        user_firstName = data.user_firstName,
        user_mobileNumber = data.user_mobileNumber,
        user_lastName = data.user_lastName,
        user_passwrd =hashed_pw
        
    )


    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user
