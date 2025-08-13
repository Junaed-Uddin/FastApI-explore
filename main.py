import sys, os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI, Depends, status, Response, HTTPException
from database import engine, SessionLocal
from typing import List
import schemas, models
from sqlalchemy.orm import Session, relationship
from hashing import Hash


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/", tags=["roots"])
def root():
    return {
        "data": "route created successfully"
    }
    
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    
    
@app.post("/blog", status_code= status.HTTP_201_CREATED, tags=["blogs"])
def create_blogs(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = blog.title, description = blog.description, 
                           publisher = blog.publisher, category = blog.category,
                           time = blog.time, isPublished = blog.isPublished,
                           price = blog.price, user_id = 1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
   
    
    
@app.get("/blog", tags=["blogs"]) # response_model = List[schemas.BlogShow]
def all_blogs(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog
    

@app.get("/blog/{id}", status_code = 200, tags=["blogs"]) # response_model = schemas.BlogShow
def single_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()  # .first() or .all()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with the id {id} is not exist")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with the id {id} is not exist"}
    return blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def blog_delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"The blog id {id} is not found")
        
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        "data":{f"The blog with id {id} successfully deleted"}
    } 
    
    
@app.put("/blog/{id}", status_code = status.HTTP_202_ACCEPTED, tags=["blogs"])
def blog_update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"The blog id {id} is not found")
        
    blog.update(request.model_dump())
    db.commit()
    return "Updated Successfully"
 


@app.post("/users", response_model = schemas.UserShow, tags=["users"], status_code = status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    
    data = user.model_dump()
    # print(data)
    data["password"] = Hash.bcrypt(user.password)
    new_user = models.User(**data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users", response_model = List[schemas.UserShow], tags=["users"])
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get("/users/{id}", response_model = schemas.UserShow, tags=["users"])
def singleUser(id: int, db: Session = Depends(get_db)):
    single_user = db.query(models.User).filter(models.User.id == id).first()
    
    if not single_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"The blog id {id} is not found")
    return single_user

