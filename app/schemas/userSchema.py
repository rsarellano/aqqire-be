from pydantic import BaseModel

class UserBase(BaseModel):
    user_email: str
    user_firstName: str
    user_lastName: str
    user_passwrd: str
    user_mobileNumber: str | None = None

class UserCreate(UserBase):
    id: int


    class Config:
        orm_mode=True
        # from_attributes = True