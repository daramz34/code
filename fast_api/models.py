from sqlalchemy import Column, Integer, String, Float
from fast_api.database import Base

class Item(Base):
     __tablename__ = "items"  # Table name in SQLite
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String, index=True)
     description = Column(String)
     price = Column(Float)