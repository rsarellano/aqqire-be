from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    user_email: str
    user_firstName: str
    user_lastName: str
    

class UserCreate(UserBase):
   
    user_passwrd: str

class UserLogin(BaseModel):
    user_email: EmailStr
    user_passwrd: str

class UserResponse(UserBase):
    id: int

    class config:
        orm_mode=True
        from_attribute = True