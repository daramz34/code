#from sqlalchemy.orm import Session
from models import Items
#from schemas import ItemResponse, ItemCreate
from database import SessionLocal



def create_item(name:str, price:str, description:str):
    db = SessionLocal()
    items = Items(name=name, price =price, description=description)
    db.add(items)
    db.commit()
    db.refresh(items)
    db.close()
    return items



def get_item():
    db = SessionLocal()
    items = db.query(Items).all()
    db.close()
    return items

def delete_item(item_id:int):
    db = SessionLocal()
    items = db.query(Items).filter(Items.id == item_id).first()

    if not items:
        db.close()
        return None
    
    db.delete(items)
    db.commit()
    db.close()
    return True