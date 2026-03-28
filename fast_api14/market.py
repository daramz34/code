from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fast_api14.schemas import Itemcreate, ItemResponse
from fast_api14.models import Student
from fast_api14.database import get_db
from fast_api14.crud import create_item, get_all_items



router= APIRouter(prefix="/market", tags=["MARKET"])

@router.post("/", response_model=ItemResponse)
def create_item_routes(item: Itemcreate, db: Session= Depends(get_db)):
    student = db.query(Student).filter(Student.id == item.owner_id).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="No student found with this id"
        )
    return create_item(db=db, item=item)

@router.get("/{item_id}", response_model=list[ItemResponse])
def get_item_routes(skip: int,limit:int =10, db:Session=Depends(get_db)):
    yay = get_all_items(db=db, skip=skip, limit=limit )
    if not yay:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return yay