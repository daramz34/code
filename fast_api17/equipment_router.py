from fastapi import APIRouter, Depends
from fast_api17.schemas import EquipmentCreate, EquipmentResponsre
from sqlalchemy.orm import Session
from fast_api17.database import get_db
from fast_api17.crud import get_equipmenT, create_equipment


router = APIRouter(prefix="/equipment", tags=["Equipment"])



@router.post("/", response_model=EquipmentResponsre)
def create_equipment_router(equip: EquipmentCreate, db:Session=Depends(get_db)):
    return create_equipment(equip=equip, db=db)


@router.get("/", response_model=list[EquipmentResponsre])
def get_equipment_router(db:Session = Depends(get_db)):
    return get_equipmenT(db=db)