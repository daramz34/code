from pydantic import BaseModel, EmailStr



class UserCreate(BaseModel): # for registration
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel): # for login
    username:str
    password: str

class TokenResponse(BaseModel):
    access_token : str 
    token_type: str ="bearer"