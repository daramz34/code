from fast_api8.database import SessionLocal, engine,Base
from fast_api8.models  import Items
from fast_api8.schemas import ItemCreate, ItemResponse
from fast_api8.crud import create_item, get_item, delete_item
from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create(item:ItemCreate, db: Session = Depends(get_db)):
    return create_item(
        db=db, item=item
    )



@app.get("/items/", response_model=list[ItemResponse])
def get(db: Session = Depends(get_db)):
    return get_item(db=db)


@app.delete("/items/{item_id}", status_code=status.HTTP_202_ACCEPTED)
def delete(item_id: int, db: Session = Depends(get_db)):
    result = delete_item(db=db, item_id=item_id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
              detail="Item not found")
    

    return None
    