from fastapi import FastAPI
import router_learn.bank as bank




app = FastAPI()

app.include_router(bank.router)


