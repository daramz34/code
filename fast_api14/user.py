from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fast_api14.schemas import StudResponse, StudCreate
from fast_api14.models import Student
from fast_api14.database import get_db
from fast_api14.crud import create_stud_data, get_stud


router = APIRouter(prefix="/students", tags=["STUDENTS"])



@router.post("/", response_model=StudResponse)
def create_student(student: StudCreate, db: Session = Depends(get_db)):
    return create_stud_data(db=db, stud=student)


@router.get("/", response_model=list[StudResponse])
def get_all_students(db:Session= Depends(get_db)):
    return get_stud(db=db)

