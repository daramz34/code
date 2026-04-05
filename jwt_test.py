from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from pydantic import BaseModel
from passlib.context import CryptContext


app = FastAPI()

SECRET = "mybankai_secret_key_32bytes_long"
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


users = {
    "daramz": pwd_context.hash("password123"),
    "john": pwd_context.hash("john456")
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
        raise HTTPException(status_code=401, detail="invalid token")
    



@app.post("/login")
def Login(data: LoginData):
    if data.username not in users: 
        raise HTTPException(status_code=401, detail="invalid username or password")
    
    if not pwd_context.verify(data.password, users[data.username]):
        raise HTTPException(status_code=401, detail="invalid username or password")
    
    token = jwt.encode({"username": data.username}, SECRET, algorithm=ALGORITHM)

    return {"Access_token": token}

@app.get("/secret")
def secret_route(current_user: dict= Depends(check_token)):
    return{
        "Message": "BOYAHH",
        "user": current_user["username"]
    }