from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
import schemas, models
from database import get_db
from repositories import blog
import oauth2

router = APIRouter(
    prefix = "/blog",
    tags = ["Blogs"]
)


# show all blogs
@router.get("/") # response_model = List[schemas.BlogShow]
def all_blogs(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], 
              db: Session = Depends(get_db)):
    return blog.show_all(db)



# create blog
@router.post("/", status_code= status.HTTP_201_CREATED)
def create_blog(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)



# show single blog
@router.get("/{id}", status_code = 200, response_model = schemas.BlogShow) # response_model = schemas.BlogShow
def single_blog(id: int, current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Session = Depends(get_db)):
    return blog.show_single(id, db)



# delete blog
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def blog_delete(id: int, current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Session = Depends(get_db)):
    return blog.delete(id, db)
    
    
    
# update blog 
@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def blog_update(id: int, current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)
 
