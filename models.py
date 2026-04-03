from sqlalchemy import Column, String, Integer
from database import Base


class Auth(Base):
    __tablename__ = "Auth"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)