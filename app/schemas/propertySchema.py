
from pydantic import BaseModel

class PropertyBase(BaseModel):
    name: str
    city: str
    state: str
    type: str
    price: int
    address: str

class PropertyCreate(PropertyBase):
    id: int
 

    class config:
        orm_mode =True
        from_attribute = True