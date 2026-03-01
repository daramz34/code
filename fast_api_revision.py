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






# from fastapi import FastAPI

# app = FastAPI()



# @app.get("/about")
# def about():
#     return {
#         "name" : "Task Manager API",
#         "description" : "Manage daily tasks efficiently",
#         "author" : "Daramz",
#         "features" : ["create", "read", "update", "delete", "filter"]    
#         }

# @app.get("/status")
# def status():
#     return {
#         "status": "operational",
#         "database": "connected",
#         "version": "1.0",
#         "uptime" : "99.9%"
#     }

# @app.get("/routes")
# def routes():
#     return {
#         "endpoints": [
#         {"path": "/about", "method": "GET", "description": "API information"},
#         {"path": "/status", "method": "GET", "description": "Health check"},
#         {"path": "/routes", "method": "GET", "description": "This list"}]
# }

# @app.get("/docs")
# def docs():
#     return {
#         "message": "Interactive API documentation",
#         "url": "http://127.0.0.1:8000/docs",
#         "alternative": "http://127.0.0.1:8000/redoc"
#     }





# # calculator api with path parameters


# from fastapi import FastAPI
# from fastapi import Path


# app = FastAPI()



# @app.get("/math/add/{a}/{b}")
# def add(a: int, b: int):
#     return {
#         "operation" : "add",
#         "a" : a,
#         "b" : b,
#         "result ": a + b
#         }


# @app.get("/math/subtract/{a}/{b}")
# def sub(a: int, b: int):
#     return {
#         "operation" : "subtraction",
#         "a" : a,
#         "b" : b,
#         "result ": a - b
#     }

# @app.get("/math/multiply/{a}/{b}")
# def multiply(a:int, b:int):
#     return {
#         "operation" : "multiplication",
#         "a" : a,
#         "b" : b,
#         "result": a * b
#     }

# @app.get("/math/divide/{a}/{b}")
# def div(a:int, b:int):
#     if b == 0:
#         return {"error": "Cannot divide by Zero",
#                 "a":a, "b":b}
#     return {
#         "operation" : "divide",
#         "a" : a,
#         "b" : b,
#         "result": a / b
        
#     }

# @app.get("/math/power/{base}/{exp}")
# def pow(base:int = Path(..., ge=0, le=10), 
#         exp:int= Path(..., ge=0, le=10)):
#     return {
#         "The power is": base**exp
#     }

# @app.get("/math/mod/{a}/{b}")
# def mod(a:int, b:int):
#     return {
#         "The modulo is": a % b
#     }

# @app.get("/text/upper/{text}")
# def uppercase(text: str):

#     return {
#         "uppercase version" : text.upper()
#     }

# @app.get("/text/reverse/{text}")
# def reverse(text: str):
#     reversed_text = text[::-1]
#     length = len(text)
#     return {
#        "original" : text,
#         "reversed" : reversed_text,
#         "length" : length
        
#     }
    

# @app.get("/text/len/{text}")
# def length(text: str):
  
#     return {
#         "character count" : len(text)
#     }

# @app.get("/text/words/{sentence}")
# def word_count(sentence: str):
#     return {
#         "character count" : len(sentence.split())
#     }





# #ery parameters

# from fastapi import FastAPI, Query
# from typing import Optional

# app = FastAPI()

# products =[
#     {"id": 1, "name": "Laptop", "category": "tech", "price": 999.99, "stock": 5},
#     {"id": 2, "name": "Phone", "category": "tech", "price": 699.99, "stock": 10},
#     {"id": 3, "name": "Headphones", "category": "tech", "price": 199.99, "stock": 0},
#     {"id": 4, "name": "T-Shirt", "category": "clothing", "price": 29.99, "stock": 50},
#     {"id": 5, "name": "Jeans", "category": "clothing", "price": 59.99, "stock": 30},
#     {"id": 6, "name": "Sneakers", "category": "clothing", "price": 89.99, "stock": 15},
#     {"id": 7, "name": "Coffee Maker", "category": "home", "price": 79.99, "stock": 8},
#     {"id": 8, "name": "Blender", "category": "home", "price": 49.99, "stock": 12},
# ]

# @app.get("/products")
# def get_products(q: Optional[str] = None ):
#     results = products
    
#     if q:
#         results = [p for p in results if q.lower() in p["name"].lower()]
#     return{ "count": len(results),
#            "filters" : {"q":  q},
#            "results": [results]
        
#     }


# @app.get("/products/categories")
# def get_categories():
    


# wasnt able to get query






#UNDERSTANDING QUERY MORE






# from fastapi import FastAPI, Query
# from typing import Optional

# app = FastAPI()

# @app.get("/items/")
# def get_items(q: Optional[str] = None):
#     if q:
#         return {"searching": q}
#     return {"all_items": "showing"}


# # @app.get("/products/")
# # def search(limit: int = Query(10, ge=1, le=100), min_price: float = Query(0, ge=0)):
# #     return {
# #         "limit": limit,
# #         "min_price" : min_price
# #     }

# # # multiple query parameters
# # @app.get("/products/")
# # def filter_products(
# #     q: Optional[str] =None,
# #     category: Optional[str] = None,
# #     min_price: float = Query(0, ge=0),
# #     max_price: float = Query(10000, ge=0),
# #     sort: str = "name",
# #     in_stock: bool = False

# # ):
# #     return {
# #         "filters" : {
# #             "q" : q,
# #             "category" : category,
# #             "min_price" : min_price,
# #             "max_price" : max_price,
# #             "sort" : sort,
# #             "in_stock" : in_stock
# #         }
# #     }


# # products = [
# #     {"name": "Laptop", "category": "tech", "price": 999},
# #     {"name": "Phone", "category": "tech", "price": 699},
# #     {"name": "Shirt", "category": "clothing", "price": 29}
# # ]

# # @app.get("/products/")
# # def search(
# #     q: Optional[str] = None,
# #     category: Optional[str] = None,
# #     max_price: float = Query(10000, ge=0)
# # ):
# #     results = products
    
# #     # Search by name
# #     if q:
# #         results = [p for p in results if q.lower() in p["name"].lower()]
    
# #     # Filter by category
# #     if category:
# #         results = [p for p in results if p["category"] == category]
    
# #     # Filter by price
# #     results = [p for p in results if p["price"] <= max_price]
    
# #     return {"count": len(results), "results": results}




# books = [
#     {"id": 1, "title": "Python", "genre": "tech", "year": 2020},
#     {"id": 2, "title": "FastAPI", "genre": "tech", "year": 2021},
#     {"id": 3, "title": "1984", "genre": "fiction", "year": 1949}
# ]

# @app.get("/books/")
# def search_books(
#     q: Optional[str] = None,
#     genre: Optional[str] = None,
#     max_year: int = Query(2024, le=2024)
#     # Query: optional search in title
#     # Query: optional filter by genre
#     # Query: optional max_year (default 2024, ≤ 2024)
# ):
#     results = books
#     if q:
#         results = [p for p in results if q.lower() in p["title"].lower()]
    
#     if genre:
#         results = [p for p in results if p["genre"] == genre]
    
#     results = [p for p in results if p["year"] <= max_year]
    
    
#     # Filter logic here
#     return {"count": len(results), "results": results}




# from fastapi import FastAPI, Query, Path
# from typing import Optional

# app = FastAPI()
# books = [
#     {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "genre": "programming", "year": 2019, "available": True, "rating": 4.8},
#     {"id": 2, "title": "Clean Code", "author": "Robert Martin", "genre": "programming", "year": 2008, "available": True, "rating": 4.7},
#     {"id": 3, "title": "1984", "author": "George Orwell", "genre": "fiction", "year": 1949, "available": False, "rating": 4.6},
#     {"id": 4, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "genre": "programming", "year": 1999, "available": True, "rating": 4.8},
#     {"id": 5, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "fiction", "year": 1960, "available": True, "rating": 4.9},
#     {"id": 6, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "fiction", "year": 1925, "available": False, "rating": 4.4},
#     {"id": 7, "title": "Introduction to Algorithms", "author": "Thomas Cormen", "genre": "computer science", "year": 2009, "available": True, "rating": 4.9},
#     {"id": 8, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "fiction", "year": 1813, "available": True, "rating": 4.6},
# ]


# @app.get("/books/")
# def search_book(
#                 q: Optional[str] = None,
#                 genre: Optional[str] = None,
#                 author: Optional[str] = None,
#                 available: Optional[bool] = None,
#                 min_rating: float = Query(0, le=5, ge=0),
#                 min_year: int = Query(1800, ge=1800),
#                 max_year: int = Query(2024, le=2024),
#                 sort: str = "title",
#                 limit: int = Query(10, gt=0, lt=21)
# ):
#     results = books
#     if q:
#         results = [p for p in results if q.lower() in p["title"].lower()]
    
#     if genre:
#         results = [p for p in results if p["genre"].lower() == genre.lower()]
        
#     if author:
#         results = [p for p in results if author.lower() in p["author"].lower() ]
    
#     if available is not None:
#         results = [p for p in results if p["available"] == available]

#     results = [p for p in results if p["rating"] >= min_rating]

#     results = [p for p in results if min_year <= p["year"] <= max_year]


#     if sort == "title":
#         results.sort(key=lambda x: x["title"])
#     elif sort == "year":
#         results.sort(key=lambda x: x["year"])
#     elif sort == "rating":
#         results.sort(key=lambda x: x["rating"])
#     elif sort == "-rating":
#         results.sort(key=lambda x: x["rating"], reverse= True)




#     return {
#     "count": len(results),
#     "filters": {
#         "q": q,
#         "genre": genre,
#         "author": author,
#         "available": available,
#         "min_rating": min_rating,
#         "min_year": min_year,
#         "max_year": max_year,
#         "sort": sort,
#         "limit": limit
#     },
#     "results": results[:limit]  # Actually apply limit!
# }

# @app.get("/books/{book_id}")
# def get_book(book_id: int = Path(gt=0)):
#     for book in books:
#         if book["id"] == book_id:
#             return {
#                 "results" : book
#             }
#     return {"error": "Not found"}

# @app.get("/genres/")
# def get_genres():
#     genres = list(set(b["genre"] for b in books))
#     return {"genres": genres}

# @app.get("/authors/")
# def get_authors(sort: str = "name"):
#     # Count books per author
#     author_counts = {}
#     for b in books:
#         author_counts[b["author"]] = author_counts.get(b["author"], 0) + 1
    
#     authors = [{"name": name, "book_count": count} for name, count in author_counts.items()]
    
#     if sort == "book_count":
#         authors.sort(key=lambda x: x["book_count"], reverse=True)
#     else:  # name
#         authors.sort(key=lambda x: x["name"])
    
#     return {"authors": authors}