from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from crud import create_user, get_user
from schemas import UserCreate, UserResponse



router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=UserResponse,
             description="Enter user info")
def create_user_router(user: UserCreate, db:Session= Depends(get_db)):
    return create_user(db=db, user=user)


@router.get("/", response_model=list[UserResponse])
def get_user_router(db:Session= Depends(get_db)):
    return get_user(db=db)