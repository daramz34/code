from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fast_api19.crud import create_user, authenticate_user
from fast_api19.models import User
from fast_api19.database import get_db
import jwt, os
from fast_api19.schemas import UserCreate, LoginRequest, TokenResponse
from dotenv import load_dotenv



router = APIRouter(prefix="/auth", tags=["AUth"])

load_dotenv()
SECRET = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

security = HTTPBearer()


def check_token(credentials: HTTPAuthorizationCredentials= Depends(security)):
    try: 
        payload = jwt.decode(credentials.credentials, SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    


@router.post("/register")
def sign_in(user: UserCreate, db: Session= Depends(get_db)):
    return create_user(db=db, user=user)


@router.post("/login")
def login(request: LoginRequest, db: Session= Depends(get_db)):
    user = authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    token = jwt.encode(
        {"username": request.username}, SECRET, algorithm=ALGORITHM
    )
    return {"access_token": token,
            "token_type": "bearer"}


@router.get("/secret")
def secret_route(user: dict = Depends(check_token)):
    return{
        "Message": "Welcome You have access to this proetected route",
        "user_id": user
    }