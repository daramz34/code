from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas, models


router = APIRouter(prefix="/market", tags=["MARKET"])

@router.post("/", response_model=schemas.ItemResponse)
def list_item_on_market(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == item.owner_id).first()
    if not student:
        raise HTTPException(
            status_code=404, 
            detail=f"Oga, Student with ID {item.owner_id} not found. You can't list an item without a valid owner!"
        )
    
    return crud.create_item(db=db, item=item)

@router.get("/", response_model=list[schemas.ItemResponse])
def view_market_feed(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    # Returns items WITH their nested student info
    return crud.get_all_items(db=db, skip=skip, limit=limit)