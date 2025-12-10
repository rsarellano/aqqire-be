from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from app.connection.database import Base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Users(Base):
    __tablename__ = "users"

    _id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    active_token = Column(String, index=True, nullable=True)
    active = Column(Boolean, index=True, nullable=False, default=True)
    can_post = Column(Boolean, index=True, nullable=False, default=True)
    city = Column(String, index=True, nullable=True)
    click_report_instruction = Column(Boolean, index=True, nullable=True, default=False)
    college_accomplishment = Column(String, index=True, nullable=True)
    
    
    
    
    
    user_email = Column(String, index=True, nullable=False)
    user_firstName = Column( String, index=True, nullable=False)
    user_lastName = Column (String, index=True, nullable=False)
    user_passwrd = Column(String, index=True, nullable=False)
    user_mobileNumber = Column(String, index=True, nullable=True)
    # user_subscription = Column(String, index=True, nullable=False)
    
    properties = relationship("Property", back_populates="owner")