
from pydantic import BaseModel

class PropertyCreate(BaseModel):
    name: str
    city: str
    state: str
    type: str
    price: int
    address: str

class PropertyResponse(PropertyCreate):
    id: int
 

    class Config:
        orm_mode =True
        from_attributes = True