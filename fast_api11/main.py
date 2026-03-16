from fastapi import FastAPI, status, HTTPException, Depends

import crud
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from schema import UserResponse, UserCreate
from typing import List
Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/url/", response_model=UserResponse, status_code=status.HTTP_200_OK)
def create_short_url(url:UserCreate, db:Session = Depends(get_db)):
    return crud.create_url(
        db=db,
          url=url)


@app.get("/url/{url_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_short_url(url_id: int, db: Session = Depends(get_db)):
    url = crud.get_url(
        db=db,
        url_id=url_id
    )
    if not url:
        raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail="url does not exist"
        )
    return url
    

@app.get("/url/", response_model=List[UserResponse])
def get_all_url(db:Session = Depends(get_db)):
    return crud.get_all_urls(db=db)




@app.delete("/url/{url_id}", status_code=status.HTTP_200_OK)
def delete_short_url(url_id: int, db:Session = Depends(get_db)):
    url = crud.delete_url(db=db, url_id=url_id)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="url does not exist"
        )
    return "Done"