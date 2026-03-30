from fastapi import FastAPI
import user_routes, equipment_routes
from database import Base, engine


app= FastAPI(
    title="CAMPUS RENTAL APP",
    description="Place for renting stuff",
    version="1.0"
)


Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(equipment_routes.router)
