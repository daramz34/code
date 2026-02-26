# intro/ get method
# from fastapi import FastAPI 

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"data": "Test"}



# @app.get("/about")
# def about():
#     return {"Data": "About"}



# path/endpoint parameters
# from fastapi import FastAPI

# app = FastAPI()

# inventory = {
#     1: {
#         "name": "milk",
#         "price": 3.00,
#         "brand" : "loya"
#     }
# }

# @app.get("/get_item/{item_id}/{name}")
# def get_item(item_id: int, name: str):
#     return f"{inventory[item_id]} name: {name}"






#PATH

# from fastapi import FastAPI, Path

# app = FastAPI()

# inventory = {
#     1: {
#         "name": "milk",
#         "price": 3.00,
#         "brand" : "loya"
#     }
# }

# @app.get("/get_item/{item_id}")
# def get_item(item_id: int = Path(..., description="The ID of the item you like to view", gt=0,lt=2)): # constraints gt = greater than lt = less than ge = greater than or equal to le = less than or equal to
#     return inventory[item_id]





# Query Parameters --> ?,&
# from fastapi import FastAPI, Path
# from typing import Optional
# app = FastAPI()

# inventory = {
#     1: {
#         "name": "milk",
#         "price": 3.00,
#         "brand" : "loya"
#     }
# }

# @app.get("/get_item/{item_id}")
# def get_item(item_id: int = Path(..., description="The ID of the item you like to view", gt=0,lt=2)): # constraints gt = greater than lt = less than ge = greater than or equal to le = less than or equal to
#     return inventory[item_id]

# @app.get("/get_by_name")
# def get_item(name: Optional [str] = None):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"DAta": "Not found"}


# @app.get("/get_by_name_test")
# def get_item(*, name: Optional [str] = None, test = int): # added-test=int
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"DAta": "Not found"}



# combinig query and path parameters
# from fastapi import FastAPI, Path
# from typing import Optional
# app = FastAPI()

# inventory = {
#     1: {
#         "name": "milk",
#         "price": 3.00,
#         "brand" : "loya"
#     }
# }

# @app.get("/get_item/{item_id}")
# def get_item(item_id: int = Path(..., description="The ID of the item you like to view", gt=0,lt=2)): # constraints gt = greater than lt = less than ge = greater than or equal to le = less than or equal to
#     return inventory[item_id]


# @app.get("/get_by_name_test/{item_id}")
# def get_item(*, item_id:int,name: Optional [str] = None, test = int): 
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"DAta": "Not found"}





# #REQUEST METHOD
# from fastapi import FastAPI, Path
# from typing import Optional
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     brand: Optional[str] = None




# inventory = {

# }

# @app.get("/get_item/{item_id}")
# def get_item(item_id: int = Path(..., description="The ID of the item you like to view", gt=0)): # constraints gt = greater than lt = less than ge = greater than or equal to le = less than or equal to
#     return inventory[item_id]

# @app.get("/get_by_name")
# def get_item(name: str):
#     for item_id in inventory:
#         if inventory[item_id].name == name:
#             return inventory[item_id]
#     return {"DAta": "Not found"}


# @app.post("/create_item/{item_id}")
# def create_item(item_id: int, item: Item):
#     if item_id in inventory:
#         return {"Error": "Item id already exists"}
    
#     # inventory[item_id] = {"name": item.name, "brand": item.brand, "Price": item.price}
#     inventory[item_id] = item
#     return inventory[item_id]




# #Put method & delete
# from fastapi import FastAPI, Path, Query
# from typing import Optional
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     brand: Optional[str] = None

# class UpdateItem(BaseModel):
#     name: Optional[str] = None
#     price: Optional[float] = None
#     brand: Optional[str] = None






# inventory = {

# }

# @app.get("/get_item/{item_id}")
# def get_item(item_id: int = Path(..., description="The ID of the item you like to view", gt=0)): # constraints gt = greater than lt = less than ge = greater than or equal to le = less than or equal to
#     return inventory[item_id]

# @app.get("/get_by_name")
# def get_item(name: str):
#     for item_id in inventory:
#         if inventory[item_id].name == name:
#             return inventory[item_id]
#     return {"DAta": "Not found"}


# @app.post("/create_item/{item_id}")
# def create_item(item_id: int, item: UpdateItem):
#     if item_id in inventory:
#         return {"Error": "Item id already exists"}
    
#     # inventory[item_id] = {"name": item.name, "brand": item.brand, "Price": item.price}
#     inventory[item_id] = item
#     return inventory[item_id]

# @app.put("/update-item/{item_id}")
# def update_item(item_id: int, item: Item):
#     if item_id not in inventory:
#         return {"Error": "Item id does not  exists"}
    
#     if item.name != None:
#         inventory[item_id].name = item.name
#     if item.price != None:
#         inventory[item_id].price = item.price
#     if item.brand != None:
#         inventory[item_id].brand = item.brand
#     return inventory[item_id]


# @app.delete("/delete_item")
# def delete_item(item_id: int = Query(..., description="the id of the item to delete", gt=0)):
#     if item_id not in inventory:
#         return {"Error": "Id does not exists"}
#     del inventory[item_id]
#     return {"Success": "item deleted!!"}









# #Return status code and error response
# from fastapi import FastAPI, Path, Query, HTTPException, status
# from typing import Optional
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     brand: Optional[str] = None

# class UpdateItem(BaseModel):
#     name: Optional[str] = None
#     price: Optional[float] = None
#     brand: Optional[str] = None






# inventory = {

# }

# @app.get("/get_item/{item_id}")
# def get_item(item_id: int = Path(..., description="The ID of the item you like to view", gt=0)): # constraints gt = greater than lt = less than ge = greater than or equal to le = less than or equal to
#     return inventory[item_id]

# @app.get("/get_by_name")
# def get_item(name: str):
#     for item_id in inventory:
#         if inventory[item_id].name == name:
#             return inventory[item_id]
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item name not found") ###


# @app.post("/create_item/{item_id}")
# def create_item(item_id: int, item: UpdateItem):
#     if item_id in inventory:
#        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="item id already exist found") ###

#     # inventory[item_id] = {"name": item.name, "brand": item.brand, "Price": item.price}
#     inventory[item_id] = item
#     return inventory[item_id]

# @app.put("/update-item/{item_id}")
# def update_item(item_id: int, item: Item):
#     if item_id not in inventory:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item id does not exist") ###

    
#     if item.name != None:
#         inventory[item_id].name = item.name
#     if item.price != None:
#         inventory[item_id].price = item.price
#     if item.brand != None:
#         inventory[item_id].brand = item.brand
#     return inventory[item_id]


# @app.delete("/delete_item")
# def delete_item(item_id: int = Query(..., description="the id of the item to delete", gt=0)):
#     if item_id not in inventory:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item does not exists ") ###

#     del inventory[item_id]
#     return {"Success": "item deleted!!"}







# from fastapi import FastAPI
# from datetime import datetime

# app = FastAPI()


# @app.get("/")
# def home():
#     return {"name": "daramz",
#             "version": 1.0,
#             "description": "good"}

# @app.get("/health")
# def health():
#     return {"status" : "Healthy",
#             "uptime": "100%"}

# @app.get("/time")
# def time():
#     return{"timestamp": datetime.now().isoformat(),
#            "timezone": "local"}

# @app.get("/author")
# def author():
#     return {"Author": "Daramz",
#             "email": "adarmz@gamil.com",
#             "github": "github.com/daramz"}






from fastapi import FastAPI

app = FastAPI()



@app.get("/about")
def about():
    return {
        "name" : "Task Manager API",
        "description" : "Manage daily tasks efficiently",
        "author" : "Daramz",
        "features" : ["create", "read", "update", "delete", "filter"]    
        }

@app.get("/status")
def status():
    return {
        "status": "operational",
        "database": "connected",
        "version": "1.0",
        "uptime" : "99.9%"
    }

@app.get("/routes")
def routes():
    return {
        "endpoints": [
        {"path": "/about", "method": "GET", "description": "API information"},
        {"path": "/status", "method": "GET", "description": "Health check"},
        {"path": "/routes", "method": "GET", "description": "This list"}]
}

@app.get("/docs")
def docs():
    return {
        "message": "Interactive API documentation",
        "url": "http://127.0.0.1:8000/docs",
        "alternative": "http://127.0.0.1:8000/redoc"
    }