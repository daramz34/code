from fastapi import FastAPI
import learn.router_learn2.router as router
from learn.router_learn2.database import Base, engine


app= FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(router.router)