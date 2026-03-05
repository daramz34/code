from pydantic import BaseModel
from typing import Optional



class Task_Create(BaseModel):
    title: str
    description: Optional[str] = None
    