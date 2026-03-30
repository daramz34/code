from sqlalchemy.orm import Session
from fast_api16.models import Equipment, User
from fast_api16.schemas import EquipmentCreate, UserCreate




def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()




def create_equipment(db:Session, equip: EquipmentCreate):
    db_equip = Equipment(**equip.model_dump())
    db.add(db_equip)
    db.commit()
    db.refresh(db_equip)
    _ = db_equip.owner
    return db_equip

def get_equipment(db: Session, skip: int= 0, limit: int= 20):
    return db.query(Equipment).offset(skip).limit(limit).all()


def get_equipment_by_id(db:Session, equip_id: str):
    return db.query(Equipment).filter(Equipment.id == equip_id).first()
