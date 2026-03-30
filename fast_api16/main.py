from fastapi import FastAPI
import fast_api16.user_routes as user_routes, fast_api16.equipment_routes as equipment_routes
from fast_api16.database import Base, engine


app= FastAPI(
    title="CAMPUS RENTAL APP",
    description="Place for renting stuff",
    version="1.0",
    contact={
        "name": "Daramz",
        "url": "https://github.com/dashboard"
    }
)


Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(equipment_routes.router)
