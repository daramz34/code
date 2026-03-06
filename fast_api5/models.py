from fast_api5.database import Base
from sqlalchemy import Integer, String, Float, Column



class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    secret_admin_note = Column(String, default="Internal-Only-Data")