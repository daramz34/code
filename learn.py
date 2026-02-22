# from fastapi import FastAPI
# catalog = {
#     "tomatoes": {
#         "units" : "boxes",
#         "qty" : 1000
#     },
#     "wines": {
#         "units" : "Bottles",
#         "qty" : 500
#     }

# }

# app = FastAPI(title = "NEW jesery APi server")

# @app.get("/warehouse/{product}")
# async def load_truck(product, order_qty):
#     return{
#         "product": product,
#         "order_qty": order_qty,
#         "units": catalog[product]["units"],
#     }



# from fastapi import FastAPI

# app = FastAPI() #creates the brain of the server

# @app.get("/") # when the client goes to the home page, this function will be called
# def say_hello(): # runs this function when the client goes to the home page
#     return {"msg": "Hello World"} # returns a dictionary with a message key and a value of "Hello World"



# revison on day4

# we used path parameters = /user/{user_id}

# type conversion = user_id: int
# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}



from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def welcome():
    return {"Message": "Welcome!!!"}

@app.get("/profile/{username}")
def create_profile(username: str):
    return {"Username": username, "Status": "Active"}

@app.get("/post/{post_id}")
def create_post(post_id: int):
    return {"Post ID": post_id, "Title": "Sample Post"}

@app.get("/product/{product_name}")
def create_product(product_name: str, price: float = 99.99):
    return {"Product": product_name, "Price": price}

