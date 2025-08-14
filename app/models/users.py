<<<<<<< HEAD
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
=======
from sqlalchemy import Colum, Integer, Boolean, String, ForeignKey
>>>>>>> 4e21ccd0929ee65cc1a8d85b91719599453d8b06
from app.connection.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    user_email = Column(String, index=True, nullable=False)
    user_firstName = Column( String, index=True, nullable=False)
    user_lastName = Column (String, index=True, nullable=False)
    user_passwrd = Column(String, index=True, nullable=False)