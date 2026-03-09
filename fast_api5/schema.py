from pydantic import BaseModel
from typing import Optional


# for the post request (input)
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# for the get request (output)
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    # excluding secret_admin_note here is the security aspect of day8

    class Config:
        from_attributes = True