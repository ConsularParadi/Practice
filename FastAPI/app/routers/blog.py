from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from repository import blog
from oauth2 import get_current_user

router = APIRouter(prefix="/blog", tags=["Blog"])

@router.get("/all", response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(get_db)):
    return blog.create(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session=Depends(get_db)):
    return blog.show(id, db)

@router.delete("/{id}")
def delete(id, db: Session=Depends(get_db)):
    return blog.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session=Depends(get_db)):
    return blog.update(id, request, db)