from sqlalchemy.orm import Session
from fast_api7.models import Item
from fast_api7.schemas import ItemCreate

def Create_item(db: Session, item: ItemCreate):
    # We don't need to pass 'id' manually; the DB does it!
    db_item = Item(
        name=item.name, 
        description=item.description, 
        price=item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session):
    return db.query(Item).all()