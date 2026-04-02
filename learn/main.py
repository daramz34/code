from fastapi import FastAPI
import fast_api17.user_router as user_router, fast_api17.equipment_router as equipment_router
from fast_api17.database import engine, Base


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