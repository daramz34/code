from fastapi import APIRouter, Depends, HTTPException
from models import User, Equipment
from database import get_db
import crud
from sqlalchemy.orm import Session
from schemas import UserCreate, EquipmentCreate, UserResponse, EquipmentResponse



router = APIRouter(prefix="/users", tags=["USERS"])

@router.post("/", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[UserResponse])
def get_users_routes(db: Session = Depends(get_db)):
    return crud.get_user(db=db)

@router.get("/by_id", response_model=UserResponse)
def get_users_by_id_routes(user_id: str, db:Session = Depends(get_db)):
    user =  crud.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return user


