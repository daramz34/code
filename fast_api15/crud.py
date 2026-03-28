from sqlalchemy.orm import Session
from fast_api15.models import Student, Item
from fast_api15.schemas import ItemCreate, StudentCreate




def create_student(db:Session, stud: StudentCreate):
    db_stud = Student(**stud.model_dump())
    db.add(db_stud)
    db.commit()
    db.refresh(db_stud)
    return db_stud


def get_all_student(db:Session):
    return db.query(Student).all()

def get_all_student_by_id(db:Session, student_id: str):
    return db.query(Student).filter(Student.id == student_id).first()



def create_item(db:Session, item: ItemCreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    _ = db_item.owner 
    return db_item
def get_all_items(db: Session, skip: int = 0, limit: int = 20):
   
    return db.query(Item).offset(skip).limit(limit).all()

def get_item_by_id(db: Session, item_id: str):
    return db.query(Item).filter(Item.id == item_id).first()