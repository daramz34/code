from fastapi import FastAPI, status, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from fast_api10.database import Base, engine, SessionLocal
import fast_api10.crud as crud
from fast_api10.schemas import Itemcreate, ItemReponse
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException





Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.exception_handler(HTTPException)
async def custom_http_exeception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error":
            {
                "message": exc.detail,
                "status": exc.status_code
            }
        }
    )



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "message" : "You sent bad data.. Checl your fields",
                "status" : 400
            }
        }
    )

@app.post("/items/", response_model=ItemReponse, status_code=status.HTTP_201_CREATED)
def create_item_routes(item:Itemcreate, db:Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/{item_id}", response_model=ItemReponse)
def get_item_routes(item_id: int, db:Session = Depends(get_db)):
    item = crud.get_item(db=db, item_id=item_id)

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="item does not exist"
        )


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item_routes(item_id: int, db: Session = Depends(get_db)):
    success = crud.delete_item(db=db, item_id=item_id)

    if not success:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Item not found"
        )
    return None

