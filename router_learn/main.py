from fastapi import FastAPI
import router_learn.user as user

app = FastAPI()


app.include_router(router=user.router)



@app.get("/")
def home():
    return {
        "Message": "Welcome to the Main App!!!"
    }