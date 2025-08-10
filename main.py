from fastapi import FastAPI, Depends
from database import engine, SessionLocal
import schemas, models
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
def about():
    return {
        "data": {
            "Name": "Junaed",
            "Designation": "Trainee - Software Engineer",
            "Salary": 8000,
            "Company": "ADN Diginet"
        }
    }
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    
@app.post("/blog")
def create_blogs(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = blog.title, description = blog.description, 
                           publisher = blog.publisher, category = blog.category,
                           time = blog.time, isPublished = blog.isPublished,
                           price = blog.price)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
    
@app.get("/blog/{blog_id}")
def single_blog(blog_id: int):
    return{
        "data": f"Blog {blog_id} published"
    }
 
 
