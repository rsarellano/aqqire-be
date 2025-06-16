from pydantic import BaseModel

class UserBase(BaseModel):
    user_email: str
    user_firstName: str
    user_lastName: str
    user_passwrd: str

class UserCreate(UserBase):
    id: int


    class config:
        orm_mode=True
        from_attribute = True