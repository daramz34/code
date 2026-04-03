from fastapi import FastAPI
import jwt

app = FastAPI()
SECRET = "mybankai_secret_key_32bytes_long"
ALGORITHM = "HS256"


payload = {
        "user_id" : 1,
        "name" : "daramz"
    }
token = jwt.encode(payload,  SECRET, algorithm=ALGORITHM)

token2 = jwt.decode(token, SECRET, algorithms=[ALGORITHM])


@app.get("/get-token")
def get_token():
    return {"token": token}

@app.get("/get_token2")
def get_token2():
    
    return {"Decoded": token2}
