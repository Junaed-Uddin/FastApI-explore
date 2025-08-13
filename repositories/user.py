from fastapi import HTTPException
import models, schemas
from sqlalchemy.orm import Session
from hashing import Hash


def show_all(db: Session):
    users = db.query(models.User).all()
    return users


def create(request: schemas.User, db: Session):
    data = request.model_dump()
    # print(data)
    data["password"] = Hash.bcrypt(request.password)
    new_user = models.User(**data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show_single(id: int, db: Session):
    single_user = db.query(models.User).filter(models.User.id == id).first()
    
    if not single_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"The blog id {id} is not found")
    return single_user