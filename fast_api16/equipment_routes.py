from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud
from models import User, Equipment
from database import get_db
from schemas import EquipmentCreate, EquipmentResponse


router = APIRouter(prefix="/equipment", tags=["EQUIPMENTS"])

@router.post("/", response_model=EquipmentResponse)
def create_equipment_route(equip: EquipmentCreate, db: Session = Depends(get_db)):
    owner = db.query(User).filter(User.id == equip.owner_id).first()

    if not owner:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"user with id does not exist"
        )
    return crud.create_equipment(db=db, equip=equip)

@router.get("/", response_model=list[EquipmentResponse])
def get_equip_routes(db: Session = Depends(get_db)):
    return crud.get_equipment(db=db)


@router.get("/by_id", response_model=EquipmentResponse)
def get_equip_by_id_routes(equid_id: str, db:Session = Depends(get_db)):
    equipment =  crud.get_equipment_by_id(db=db, equip_id=equid_id)
    if not equipment:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )
    return equipment