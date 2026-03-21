from pydantic import BaseModel
from typing import Optional



class StudBase(BaseModel):
    name : str
    major: str
    

class StudCreate(StudBase):
    pass

class StudResponse(StudBase):
    id : str
    pass

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    item_name : str
    price: float
    description: Optional[str] = None



class Itemcreate(ItemBase):
    owner_id: str
    pass

class ItemResponse(ItemBase):
    item_id : str
    owner_id: str

    owner: StudResponse
    pass

    class Config:
        from_attributes = True
