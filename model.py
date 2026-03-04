from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime


class Item(Base): # Y base?
    __tablename__ = "Items"

    id = Column(Integer, primary_key=True, index=True) # what the diff btw primary key and index
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    created = Column(DateTime, default=datetime.now)  

    #looking at this all this are column are we going to  create rows or what
    #and y is my created = Column(DateTime,) is it becuz i imported it 