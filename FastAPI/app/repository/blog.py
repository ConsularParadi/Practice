from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def show(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    return blog


def create(request: schemas, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    db.commit()
    return f"Blog with id {id} deleted"

def update(id: int, request: schemas, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).update(request, synchronize_session=False)
    db.commit()
    return "Updated Successfully"