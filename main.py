from fastapi import FastAPI
from database import engine, Base
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="JWT Auth API",
    description="Day 16 - JWT Authentication",
    version="1.0.0"
)

app.include_router(router)