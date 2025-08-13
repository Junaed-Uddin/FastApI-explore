import sys, os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from database import engine
import models
from routers import blog, user, authentication


app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)


@app.get("/", tags=["roots"])
def root():
    return {
        "data": "route created successfully"
    }
    
    

