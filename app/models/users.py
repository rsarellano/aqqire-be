from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from app.connection.database import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    user_email = Column(String, index=True, nullable=False)
    user_firstName = Column( String, index=True, nullable=False)
    user_lastName = Column (String, index=True, nullable=False)
    user_passwrd = Column(String, index=True, nullable=False)
    user_mobileNumber = Column(String, index=True, nullable=True)
    # user_subscription = Column(String, index=True, nullable=False)
    
    properties = relationship("Property", back_populates="owner")