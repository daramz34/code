from sqlalchemy import Column, String, Float, ForeignKey
import uuid
from fast_api14.database import Base
from sqlalchemy.orm import relationship



class Student(Base):
    __tablename__ = "Students"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String, nullable=False)
    major = Column(String, default="Comps")

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "Market_Items"
    item_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    owner_id = Column(String, ForeignKey("Students.id"), nullable=False) 
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    owner = relationship("Student", back_populates="items")
