from pydantic import BaseModel
from typing import Optional



class ItemCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ItemResponse(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    
    class Config:
        from_attributes = True
