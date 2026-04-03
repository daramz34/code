from fastapi import FastAPI
import jwt

app = FastAPI()
SECRET = "mybankai_secret_key_32bytes_long"
ALGORITHM = "HS256"




@app.get("/get-token")
def get_token():
    payload = {
        "user_id" : 1,
        "name" : "daramz"
    }
    token = jwt.encode(payload,  SECRET, algorithm=ALGORITHM)
    return {"token": token}
