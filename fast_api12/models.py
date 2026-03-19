from sqlalchemy import Column, String, Integer, Float
from fast_api12.database import Base


class Items(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)