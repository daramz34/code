from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fast_api18.models import Auth
from fast_api18.schemas import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")



def hash_password(password: str):
    return pwd_context.hash(password) # turns plain password to hashed string

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password) #checks if plain matches the hash


def get_user_by_username(db: Session, username:str):
    return db.query(Auth).filter(Auth.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)
    db_user= Auth(username=user.username,
        email=user.email,
        hashed_password=hashed  )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username:str, password: str):
    user = get_user_by_username(db,username)

    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
