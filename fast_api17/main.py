from fastapi import FastAPI
import user_router, equipment_router
from database import engine, Base


Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Revision",
    description="Revision on some projects",
    summary="ababababababababbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    version="9.33",
    contact={
        "Name": "DARAMZ",
        "JOB": "BACK_End_DEV"
    }
)


app.include_router(user_router.router)
app.include_router(equipment_router.router)