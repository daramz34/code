from fast_api4.database import Base
from sqlalchemy import Column,Float, Integer, String


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    # secret_code = Column(String) --> for next project







