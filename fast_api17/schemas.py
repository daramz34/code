from pydantic import BaseModel
from typing import Optional



class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
   

    class Config:
        from_attribute = True




class EquipmentCreate(BaseModel):
    item_name : str
    description: str
    daily_rate: float
    
class EquipmentResponsre(BaseModel):
    Equid_id: str
    item_name: str
    description: str
    daily_rate: float

    owner: UserResponse

    class Config:
        from_attribute = True