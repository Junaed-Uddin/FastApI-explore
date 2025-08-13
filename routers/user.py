from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
import schemas, models
from repositories import user


router = APIRouter(
    prefix = "/users",
    tags = ['Users']
)


# show all users
@router.get("/", response_model = List[schemas.UserShow])
def show_all_users(db: Session = Depends(get_db)):
    return user.show_all(db)


#  create user 
@router.post("/", response_model = schemas.UserShow, status_code = status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


# show single user 
@router.get("/{id}", response_model = schemas.UserShow)
def singleUser(id: int, db: Session = Depends(get_db)):
    return user.show_single(id, db)

