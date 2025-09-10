
from pydantic import BaseModel

class PropertyCreate(BaseModel):
    name: str
    city: str
    state: str
    type: str
    price: int
    address: str
    # status: str

class PropertyResponse(PropertyCreate):
    id: int
 

    class Config:
       
        from_attributes = True