from sqlalchemy import Column, Float, String, Integer
from fast_api13.database import Base



class Items(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)