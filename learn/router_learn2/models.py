from sqlalchemy import Column, String, Float
import uuid
from learn.router_learn2.database import Base





class Student(Base):
    __tablename__ = "Students"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index= True)
    name = Column(String, nullable=False)
    major = Column(String, default="Computer Science")