from fast_api12.database import Base
from sqlalchemy import Column, String, Float, Integer
import random, string

class URL(Base):
    __tablename__ = "Url"
    id = Column(Integer, primary_key=True, index=True)
    
      
    url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True)


    # __table_args__ = (
    #     CheckConstraint("username ~ '^[A-Za-z0-9]+$'", name="username_alphanumeric")
    # )