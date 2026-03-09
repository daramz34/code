from fast_api6.database import  Base
from sqlalchemy import Column, String, Float, Integer


class Items(Base):
    __tablename__ = "items"
    id= Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
