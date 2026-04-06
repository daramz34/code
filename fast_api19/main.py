from fastapi import FastAPI
from database import Engine, Base
from router import router


app = FastAPI(title="Security", 
              version="2.03")
Base.metadata.create_all(bind=Engine)


app.include_router(router)



@app.get("/")
def welcome():
    return{"Welcome": "user"}