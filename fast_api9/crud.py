from sqlalchemy.orm import Session
from fast_api9.model import Item
from fast_api9.schema import Itemcreate

def get_items(db: Session):
    return db.query(Item).all()

def create_item(db: Session, item:Itemcreate):
    db_item = Item(**item.model_dump()) # we used this instead of name=item.name, price=item.price...
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db:Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False