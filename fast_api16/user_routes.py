from fastapi import APIRouter, Depends, HTTPException
from fast_api16.models import User, Equipment
from fast_api16.database import get_db
import fast_api16.crud as crud
from sqlalchemy.orm import Session
from fast_api16.schemas import UserCreate, EquipmentCreate, UserResponse, EquipmentResponse



router = APIRouter(prefix="/users", tags=["USERS"])

@router.post("/", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[UserResponse])
def get_users_routes(db: Session = Depends(get_db)):
    return crud.get_user(db=db)

@router.get("/by_id", response_model=UserResponse,
            summary="Get User By ID",
            description="Fetch a specific user's profile and their equipment list using their UUID."
            )
def get_users_by_id_routes(user_id: str, db:Session = Depends(get_db)):
    user =  crud.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return user


