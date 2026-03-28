from fastapi import FastAPI
import models
from database import engine,  Base
import stud_routes, market_routes

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="BOYAHH",
    description="Campus MArketPlace API",
    version="20.4"
)

app.include_router(stud_routes.router)
app.include_router(market_routes.router)




@app.get("/")
def home():
    return{
        "Status": "online"
    }