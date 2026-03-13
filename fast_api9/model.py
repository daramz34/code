from sqlalchemy import Column, Integer, String, Float
from fast_api9.database import Base


class Item(Base):
    __tablename__ = "iTEM"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)