from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas, models
from database import get_db
from repositories import blog

router = APIRouter(
    prefix = "/blog",
    tags = ["Blogs"]
)


# show all blogs
@router.get("/") # response_model = List[schemas.BlogShow]
def all_blogs(db: Session = Depends(get_db)):
    return blog.show_all(db)



# create blog
@router.post("/", status_code= status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)



# show single blog
@router.get("/{id}", status_code = 200, response_model = schemas.BlogShow) # response_model = schemas.BlogShow
def single_blog(id: int, db: Session = Depends(get_db)):
    return blog.show_single(id, db)



# delete blog
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def blog_delete(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)
    
    
    
# update blog 
@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def blog_update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)
 
