from sqlalchemy.orm import Session
from fast_api8.models import Items
from fast_api8.schemas import ItemResponse, ItemCreate
from fast_api8.database import SessionLocal



def create_item(db: Session, item):
    
    items = Items(
        name=item.name, 
        price =item.price,
          description=item.description)
    db.add(items)
    db.commit()
    db.refresh(items)
    db.close()
    return items



def get_item(db: Session):

    return  db.query(Items).all()
    

def delete_item(db: Session, item_id:int):
    
    items = db.query(Items).filter(Items.id == item_id).first()

    if not items:
        db.close()
        return None
    
    db.delete(items)
    db.commit()
    db.close()
    return True