from sqlalchemy import Column, Integer, Boolean,String, ForeignKey
from app.connection.database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True, nullable=False)
    state = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)
    price = Column(Integer, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)

    

