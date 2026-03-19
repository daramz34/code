from sqlalchemy.orm import Session
from models import Items
from schemas import ItemCreate
from database import SessionLocal



def create_item(db:Session, item: ItemCreate):
    db_item = Items(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db:Session,
             skip: int=0,
              limit: int=5,
               max_price: float=None ):
    query = db.query(Items)
    if max_price is not None:
        query = query.filter(Items.price <= max_price)
    return query.offset(skip).limit(limit).all()

def get_items_by_id(db: Session, item_id: int):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    return db_item



def delete_item(db:Session, item_id:int):
    db_item = db.query(Items).filter(Items.id == item_id).first()

    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
    