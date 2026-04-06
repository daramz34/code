from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



Engine = create_engine("sqlite:///.security2.db")

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=Engine)

Base =declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    