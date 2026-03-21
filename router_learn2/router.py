from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from  router_learn2.models import Student
from router_learn2.database import SessionLocal

router = APIRouter(prefix="/students", tags=["STUDENTS"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def register_student(name: str, major:str, db: Session = Depends(get_db)):
    new_stu = Student(name=name, major=major)
    db.add(new_stu)
    db.commit()
    db.refresh(new_stu)
    return new_stu

@router.get("/")
def get_student(db: Session = Depends(get_db)):
    db_stud = db.query(Student).all()

    return db_stud


@router.get("/by_name/{stud_name}")
def get_student_by_name(stud_name: str, db: Session = Depends(get_db)):
    db_stud = db.query(Student).filter(Student.name == stud_name).first()
    if db_stud is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f" Student not Found"
        )
    return db_stud