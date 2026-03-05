from fastapi import FastAPI
from fast_api2.database import Base, engine
from fast_api2.model import Item
from fast_api2.crud import create_item, get_all_items


Base.metadata.create_all(bind=engine)
print("Tables created")
app = FastAPI()


@app.post("/items/")
def api_create_items(name:str, description:str, price : float):
    return create_item(name, description, price)



@app.get("/items/")
def api_get_items():
    return get_all_items()