from sqlalchemy import Column, Integer, String, Float
from database import Base



class Items(Base):
    __itemname__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    description = Column(String)
