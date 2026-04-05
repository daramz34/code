from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt

app = FastAPI()


SECRET = "my_bankai_secret_key_32bytes_long"
ALGORITHM = "HS256"

security = HTTPBearer()
users = {
    "daramz": "password1222",
    "john": "john2929"
}



class LoginData(BaseModel):
    username: str
    password: str




def check_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    



@app.post("/")
def login(data: LoginData):
    if data.username not in users:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if users[data.username] != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = jwt.encode({"username": data.username}, SECRET, algorithm=ALGORITHM)
    return {"access_token": token, 
            "token_type": "bearer"}

@app.get("/secret")
def secret_route(current_user: dict = Depends(check_token)):
    return {
        "message": "You are in",
        "user": current_user["username"]
    }