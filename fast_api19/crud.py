from sqlalchemy.orm import Session
from fast_api19.schemas import UserCreate
from fast_api19.models import User
from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hash_password: str):
   return pwd_context.verify(password, hash_password)
        

def get_user_by_username(db: Session, username:str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed=  hash_password(user.password)
    user_db = User(username = user.username,
                   email = user.email,
                   hashed_password= hashed)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def authenticate_user(db:Session, username:str, password:str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user