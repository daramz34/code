from sqlalchemy.orm import Session

from models import Items
from schemas import Itemcreate


def get_items(db:Session, skip: int=0, limit: int = 10, max_price: float = None):
    query = db.query(Items)

    if max_price is not None:
        query = query.filter(Items.price <= max_price)
    
    return query.offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Items).filter(Items.id == item_id).first()

def create_items(db:Session, item: Itemcreate):
    db_item = Items(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_items(db:Session, item_id: int):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
