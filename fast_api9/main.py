from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from fast_api9.database import SessionLocal, engine, Base
from fast_api9.model import Item
from fast_api9.schema import Itemcreate, ItemResponse
import fast_api9.crud as crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


# The "Assistant" (Dependency) to manage DB sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item_route(item: Itemcreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/", response_model=List[ItemResponse])
def get_all_items_route(db: Session = Depends(get_db)):
    return crud.get_items(db=db)



@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    success = crud.delete_item(db=db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="item not found"
        )
    return None

# almost done it just returning an empty list
#after i made some changes to my delete