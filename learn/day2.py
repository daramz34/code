from fastapi import FastAPI
app = FastAPI()

@app.get("/")

def home():
    return {"message" : "Hello World",
            "message2" : "Welcome to Day 2 of GDGOC 30 Days Challenge"}

@app.get("/about")
def info():
    return {"info": "This is a GDGOC Chanllenge API"}


@app.get("/status")
def check():
    return {"status": "up"}
