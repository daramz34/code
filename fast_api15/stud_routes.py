from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fast_api15.database import get_db
import fast_api15.crud as crud, fast_api15.schemas as schemas



router =APIRouter(prefix="/students", tags=["STUDENTS"])



@router.post("/", response_model=schemas.StudentResponse)
def create_new_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, stud=student)


@router.get("/", response_model=list[schemas.StudentResponse])
def list_students(db:Session = Depends(get_db)):
    return crud.get_all_student(db=db)