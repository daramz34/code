from fast_api2.database import SessionLocal
from fast_api2.model import Item


def create_item(name: str,
                description: str, # why not add datetime and id, and is it by force to identif them like saying str since we have already done that on models
                price: float):
    db = SessionLocal()  # should we continue calling this
    item = Item(name=name, description=description, price=price) # what is happening here
    db.add(item) #  what happend here
    db.commit() # y isnt there an argument here
    db.refresh(item)
    db.close()
    return item # y


def get_all_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items



if __name__ == "__main__": 
   
    new_item = input("Enter item name: ")
    new_item2 = input("Enter item description: ")
    new_item3 = float(input("Enter item price: "))
    new_item = create_item(new_item, new_item2, new_item3)
    print(f"Created: {new_item.name} -- ${new_item.price} (ID: {new_item.id})"
          )
    
    print("\nAll Items in the database:")
    items = get_all_items()
    for item in items:
        print(f"{item.id}: {item.name} - ${item.price}")
