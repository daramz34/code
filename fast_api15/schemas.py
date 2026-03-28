from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    item_name: str
    price: float
    owner_id: str


class StudentCreate(BaseModel):
    name: str


class StudentResponse(BaseModel):
    id: str
    name: str
    class Config:
        from_attributes = True


class ItemResponse(BaseModel):
    id: str
    item_name: str
    price: float
    owner: StudentResponse
    class Config:
        from_attributes = True