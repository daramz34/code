from sqlalchemy import Column, Integer, Float, String
from fast_api7.database import Base


class Item(Base):
    __tablename__ = "ITEMs"
    id = Column(Integer, primary_key= True, index=True)
    name = Column(String)
    price = Column(String)
    description = Column(String)

    