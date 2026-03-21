from fastapi import FastAPI
import user, market
from database import Base,  engine




app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(market.router)
