from sqlalchemy import Column, String, Float, ForeignKey
import uuid
from database import Base
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "User"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String)
    email = Column(String)

    equip = relationship("Equipment", back_populates="owner", cascade="all, delete")

class Equipment(Base):
    __tablename__ = "Equipment"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    description = Column(String)
    daily_rate = Column(Float)

    owner_id = Column(String, ForeignKey("User.id"))

    owner = relationship("User", back_populates="equip")
