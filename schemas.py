from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    description: str
    publisher: str
    category: str
    time: str
    isPublished: bool
    price: int
    
     