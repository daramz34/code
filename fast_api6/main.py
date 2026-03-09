from fast_api6.database import engine, Base, SessionLocal
from fast_api6.schema import ItemCreate, ItemResponse
from fast_api6.models import Items
from fastapi import FastAPI, status


Base.metadata.create_all(bind=engine)
app = FastAPI()



@app.post("/items/", status_code=status.HTTP_201_CREATED,
           response_model=ItemResponse )
def create_item(item: ItemCreate):
    db = SessionLocal()
    try:
        new_item = Items(
            name = item.name,
            price = item.price,
            description = item.description
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    
    finally:
        db.close()
        return new_item
    

@app.get("/items/", response_model=list[ItemResponse])
def get_item():
    db = SessionLocal()
    try: 
        items = db.query(Items).all()
        return items
    
    finally:
        db.close()




