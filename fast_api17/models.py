from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from fast_api17.database import Base
import uuid

class User(Base):
    __tablename__ = "User"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    equip = relationship("Equipment", back_populates="owner", cascade="all, delete")




class Equipment(Base):
    __tablename__ = "Equipment"
    Equip_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    item_name = Column(String)
    description = Column(String)
    daily_rate = Column(Float)


    owner_id = Column(String, ForeignKey(User.id))

    owner = relationship("User", back_populates= "equip")