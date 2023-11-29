from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Union
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine

user_router = APIRouter()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    email: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

@user_router.get("/users/", response_model=Union[List[UserBase], None])
async def get_users(db: Session = db_dependency):
    users = db.query(models.User).all()
    return [UserBase(username=user.username, email=user.email) for user in users]

@user_router.post("/users/", response_model=UserBase)
async def create_user(user: UserBase, db: Session = db_dependency):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserBase(username=db_user.username, email=db_user.email)

@user_router.get("/users/{user_id}", response_model=UserBase)
async def get_user(user_id: int, db: Session = db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return UserBase(username=user.username, email=user.email)