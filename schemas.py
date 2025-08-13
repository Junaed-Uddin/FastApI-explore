from typing import List
from pydantic import BaseModel, ConfigDict

class Blog(BaseModel):
    title: str
    description: str
    publisher: str
    category: str
    time: str
    isPublished: bool
    price: int
    
class BlogBase(BaseModel):
    title: str
    category: str
    price: int
    model_config = ConfigDict(from_attributes=True)
      

class User(BaseModel):
    name: str
    email: str
    password: str
    

class UserShow(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase]
    model_config = ConfigDict(from_attributes=True)
    

class BlogShow(BaseModel):
    title: str
    category: str
    price: int
    creator: UserShow
    model_config = ConfigDict(from_attributes=True)
    # class Config():
    #     orm_mode = True
    
    
class Login(BaseModel):
    username: str
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None