from fast_api.database import SessionLocal
from fast_api.models import Item
# db = SessionLocal() # open connection
# # do work
# db.close() # close connection

db = SessionLocal()
#create : add item to db
# item = Item(
#     name="laptop",
#     description = "Gaming laptop",
#     price = 999.99
# )
# db.add(item)

# db.commit() # actually save to database

# db.refresh(item)

# print(f"Created: {item.id}, {item.name}")

#Read
all_items = db.query(Item).all()
item = db.query(Item).filter(Item.id == 1).first()
print(item.name)

expensive = db.query(Item).filter(Item.price > 500).all()

db.close()