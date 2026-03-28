from fastapi import FastAPI
import fast_api15.models as models
from fast_api15.database import engine,  Base
import fast_api15.stud_routes as stud_routes, fast_api15.market_routes as market_routes

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