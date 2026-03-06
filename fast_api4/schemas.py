from pydantic import BaseModel
from typing import Optional



class Task_Create(BaseModel):
    name: str
    title: str
    price:  float
    description: Optional[str] = None
    