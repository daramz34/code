from pydantic import BaseModel

class URLBase(BaseModel):
    url: str
    short_code: str


class UserCreate(BaseModel):
    url: str

class UserResponse(URLBase):
    id:int
    pass
    
    class Config:
        from_attributes = True



