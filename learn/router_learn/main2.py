from fastapi import FastAPI
import learn.router_learn.bank as bank




app = FastAPI()

app.include_router(bank.router)


