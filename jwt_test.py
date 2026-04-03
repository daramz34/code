from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

app = FastAPI()
SECRET = "mybankai_secret_key_32bytes_long"
ALGORITHM = "HS256"

securiy = HTTPBearer()


def check_token(credentials: HTTPAuthorizationCredentials = Depends(securiy)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET, algorithms=ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")



@app.get("/get-token")
def get_token():
    payload = {
        "user_id" : 1,
        "name" : "daramz"
    }
    token = jwt.encode(payload,  SECRET, algorithm=ALGORITHM)
    return {"token": token}

@app.get("/secret")
def secret_route(current_user: dict = Depends(check_token)):
    
    return {"Message": "You are in",
            "user": current_user}
