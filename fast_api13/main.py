from fastapi import FastAPI, status, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from fast_api13.database import SessionLocal, Base, engine
import fast_api13.crud as crud
from fastapi.exceptions import RequestValidationError
from fast_api13.schemas import ItemCreate, ItemResponse
from fastapi.responses import JSONResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "Message": exc.detail,
                "Status" : exc.status_code
            }
        }
    )
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "Error" : {
                "message" : "You sent bad data.. Check your fields",
                "status" : 400
            }
        }
    )

@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def create_items_routes(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_items_by_idroutes(item_id: int, db:Session = Depends(get_db)):
    item = crud.get_items_by_id(db=db, item_id=item_id)
    
    if not item:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Item not found"
        )
    return item
        


@app.get("/items/", response_model=list[ItemResponse])
def get_items_routes(
    skip: int,
    limit: int,
    max_price: float = None,
    db:Session = Depends(get_db)
):
    return crud.get_item(db=db, skip=skip, limit=limit, max_price=max_price)



@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delte_items_routes(item_id: int, db:Session = Depends(get_db)):
    item = crud.delete_item(db=db, item_id=item_id)
    if not item:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Item not found"
        )
    return None 
