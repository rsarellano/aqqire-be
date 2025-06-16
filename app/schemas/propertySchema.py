
from pydantic import BaseModel

class PropertyBase(BaseModel):
    property_name: str
    property_city: str
    property_state: str
    property_type: str
    property_price: int

class PropertyCreate(PropertyBase):
    id: int
 

    class config:
        orm_mode =True
        from_attribute = True