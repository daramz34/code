from fastapi import FastAPI
import router_learn2.router as router
from router_learn2.database import Base, engine


app= FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(router.router)