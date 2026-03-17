from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class Itemcreate(ItemBase):
    pass

class Itemresponse(ItemBase):
    id: int
    pass
    
    class Config:
        from_attributes = True
