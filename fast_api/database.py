from sqlalchemy import create_engine # engine
from sqlalchemy.orm import sessionmaker # session
from sqlalchemy.ext.declarative import declarative_base #base



engine = create_engine("sqlite:///.items.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine, )

Base = declarative_base()


