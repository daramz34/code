from sqlalchemy.orm  import Session
from models import Items
from schemas import Itemcreate


def get_item(db:Session):
    return db.query(Items).all()

def create_item(db:Session, item: Itemcreate):
    db_item = Items(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db:Session, item_id:int):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False