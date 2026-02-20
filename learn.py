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



from fastapi import FastAPI

app = FastAPI() #creates the brain of the server

@app.get("/") # when the client goes to the home page, this function will be called
def say_hello(): # runs this function when the client goes to the home page
    return {"msg": "Hello World"} # returns a dictionary with a message key and a value of "Hello World"
