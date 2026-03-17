from fastapi import FastAPI, Depends, status, HTTPException
import crud
from models import Items
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from schemas import Itemcreate, Itemresponse



Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=Itemresponse, status_code=status.HTTP_200_OK)
def create_item_routes(item: Itemcreate, db:Session = Depends(get_db)):
    return crud.create_items(db=db, item=item)

@app.get("/items/", response_model=list[Itemresponse])
def read_items_routes(
    skip: int = 0,
    limit: int = 10,
    max_price: float = None,
    db:Session= Depends(get_db)
):
    return crud.get_items(db=db, skip=skip, limit=limit, max_price=max_price)


@app.get("/items/{item_id}", response_model=Itemresponse)
def read_single_item_routes(item_id: int, db:Session = Depends(get_db)):
    item = crud.get_item_by_id(db=db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "item does not exist"
        )
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item_routes(item_id: int, db:Session = Depends(get_db)):
    item = crud.delete_items(db=db, item_id=item_id)

    if not item:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Item not found"
        )
    return None
