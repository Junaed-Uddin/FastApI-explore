from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException


def show_all(db: Session):
    blog = db.query(models.Blog).all()
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title = request.title, description = request.description, 
                           publisher = request.publisher, category = request.category,
                           time = request.time, isPublished = request.isPublished,
                           price = request.price, user_id = 1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
    
def show_single(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()  # .first() or .all()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with the id {id} is not exist")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with the id {id} is not exist"}
    return blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"The blog id {id} is not found")
        
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        "data":{f"The blog with id {id} successfully deleted"}
    } 
    
    
def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"The blog id {id} is not found")
        
    blog.update(request.model_dump())
    db.commit()
    return "Updated Successfully"