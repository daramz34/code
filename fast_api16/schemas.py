from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
class UserResponse(BaseModel):
    id: str
    username: str
    email: str

    class Config:
        from_attributes = True



class EquipmentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    daily_rate: float
    owner_id: str

class EquipmentResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    daily_rate: float

    owner: UserResponse

    class Config:
        from_attributes = True
