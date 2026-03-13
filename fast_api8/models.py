from sqlalchemy import Column, Integer, String, Float
from fast_api8.database import Base



class Items(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    description = Column(String)
