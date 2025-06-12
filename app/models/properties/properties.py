from sqlalchemy import Column, Integer, Boolean,String, ForeignKey
from app.connection.database import Base

class Property(Base):
    _tablename_ = "properties"

    id = Column(Integer,primary_key=True,index=True)
    property_name = Column(String, index=True, nullable=False)
    property_state = Column(String, index=True, nullable=False)
    property_city = Column(String, index=True, nullable=False)
    property_type = Column(String, index=True, nullable=False)

    

