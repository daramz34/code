from database import Base
from sqlalchemy import Column, Integer, Float, String

class Items(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)