from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from fast_api15.database import Base
import uuid


class Student(Base):
    __tablename__ = "Students"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)

    items = relationship("Item", back_populates="owner", cascade="all, delete")


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    item_name = Column(String)
    price = Column(Float)

    owner_id =Column(String, ForeignKey("Students.id"))

    owner = relationship("Student", back_populates="items")