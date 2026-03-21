from fastapi import FastAPI
import fast_api14.user as user, fast_api14.market as market
from fast_api14.database import Base,  engine




app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(market.router)
