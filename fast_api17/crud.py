from schemas import UserCreate, EquipmentCreate
from sqlalchemy.orm import Session
from models import User, Equipment
from security import get_password_hash




def create_user(db:Session, user: UserCreate):
    hashed_pwd = get_password_hash(user.password)


    db_user = User(username = user.username,
                   email=user.email,
                   hashed_password=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db:Session):
    return db.query(User).all()



def create_equipment(db:Session, equip: EquipmentCreate):
    db_equip = Equipment(**equip.model_dump())
    db.add(db_equip)
    db.commit()
    db.refresh(db_equip)
    _ = db_equip.owner
    return db_equip


def get_equipmenT(db:Session):
    return db.query(Equipment).all()
    