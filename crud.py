from sqlalchemy.orm import Session
from fast_api14.database import Base
from fast_api14.schemas import StudCreate, StudResponse, Itemcreate, ItemResponse
from fast_api14.models import Student, Item




def create_stud_data(db:Session, stud: StudCreate):
    db_stud = Student(**stud.model_dump())
    
    db.add(db_stud)
   
    db.commit()
    db.refresh(db_stud)
   
    return db_stud

def get_stud(db:Session):
    db_stud = db.query(Student).all()
    return db_stud



def create_item(db:Session, item: Itemcreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    _ = db_item.owner
    return db_item


def get_all_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()





# def create_stud_data(db:Session, stud: StudCreate, item:Itemcreate):
#     db_stud = Student(**stud.model_dump())
#     db_item = Item(**item.model_dump())
#     db.add(db_stud, db_item)
#     #db.add(db_item)
#     db.commit()
#     db.refresh(db_stud, db_item)
#     #db.refresh(db_item)
#