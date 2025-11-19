from pydantic import BaseModel,EmailStr
from uuid import UUID
from typing import Optional

class UserBase(BaseModel):
    user_email: str
    user_firstName: str
    user_lastName: str
    user_mobileNumber: str

class UserCreate(UserBase):
   
    user_passwrd: str

class UserLogin(BaseModel):
    user_email: str
    user_passwrd: str

class UserResponse(UserBase):
    id: UUID

    class config:
        orm_mode=True
        from_attributes = True