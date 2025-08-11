from pydantic import BaseModel, ConfigDict

class Blog(BaseModel):
    title: str
    description: str
    publisher: str
    category: str
    time: str
    isPublished: bool
    price: int
    
     
class BlogShow(BaseModel):
    title: str
    category: str
    price: int
    model_config = ConfigDict(from_attributes=True)
    # class Config():
    #     orm_mode = True
    

class User(BaseModel):
    name: str
    email: str
    password: str
    

class UserShow(BaseModel):
    name: str
    email: str
    model_config = ConfigDict(from_attributes=True)