# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    imageSrc = Column(String(255), nullable=True)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    street = Column(String(100), nullable=True)
    zipcode = Column(Integer, nullable=True)
    city = Column(String(50), nullable=True)
    phoneNumber = Column(String(20), nullable=True)
    mail = Column(String(100), nullable=True)
    labels = Column(String(255), nullable=True)
    notes = Column(String(255), nullable=True)


