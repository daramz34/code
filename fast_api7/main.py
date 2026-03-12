from fast_api7.database import SessionLocal, engine, Base
from fast_api7.schemas import ItemCreate, ItemResponse
from fast_api7.models import Item
from sqlalchemy.orm import Session
from fastapi import FastAPI, status, Depends
from fast_api7.crud import Create_item, get_item



Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()


@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item:ItemCreate, db: Session =  Depends(get_db)):
    return Create_item(
        db=db, item=item
    )


@app.get("/items/", response_model=list[ItemResponse])
def get_it(db: Session = Depends(get_db)):
    return get_item(db=db)