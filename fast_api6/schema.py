from pydantic import BaseModel, Field
from typing import Optional


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Name can't be empty")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    description: Optional[str] = Field(None, description="Optional description")


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] 
    
    class Config:
        from_attributes = True

