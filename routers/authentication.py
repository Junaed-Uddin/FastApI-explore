from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
import models, schemas, auth_token
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.orm import Session
from hashing import Hash


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post("/")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"the user: '{request.username}' is not found")
        
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = "Invalid Password")
        
    access_token_expires = timedelta(minutes=auth_token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")