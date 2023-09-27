from fastapi import Response, HTTPException, status
import schemas, models
from sqlalchemy.orm import Session
from hashing import Hash

def create(request: schemas, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, response: Response, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
        # Other way
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"Blog with id {id} is not available"
    return user