from sqlalchemy import Column, Integer, Boolean,String, ForeignKey
from app.connection.database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)
    price = Column(Integer, index=True, nullable=False)
    # status = Column(String, index=True, nullable=False)

    # # location
    # international = Column(Boolean, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    state = Column(String, index=True, nullable=False)
    # zip = Column(String,index=True, nullable=False)
    # longtitude = Column(Integer, index=True, nullable=False)
    # latitude = Column(Integer, index=True, nullable=False)

    # # Common info
    # buildingSizeinSqFt = Column(String, index=True, nullable=False)
    # numberOfBuildings = Column(String, index=True, nullable=False)
    # numberOfUnits = Column(String, index=True, nullable=False)
    # numberOfFloors = Column(String, index=True, nullable=False)
    # yearBuilt = Column(String, index=True, nullable=False)
    # yearRenovated = Column(String, index=True, nullable=False)
    # lotSizeAcre = Column(String, index=True, nullable=False)
    # permitZoning = Column(String, index=True, nullable=False)
    # netRentableArea = Column(String, index=True, nullable=False)
    # buildingClass = Column(String, index=True, nullable=False)
    # netLease = Column(String, index=True, nullable=False)
    # tenancy = Column(String, index=True, nullable=False)
    # apnId = Column(String, index=True, nullable=False)
    # pricePerSquareFt = Column(String, index=True, nullable=False)
    # netOperatingIncome = Column(String, index=True, nullable=False)
    # capRate = Column(String, index=True, nullable=False)
    # occupancy = Column(String, index=True, nullable=False)
    # grossRentalIncome = Column(String, index=True, nullable=False)
    # netRentalIncome = Column(String, index=True, nullable=False)

