from sqlalchemy.orm import Session
from app import models, schemas
from typing import List

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        hashed_password=user.password,  
        email=user.email,
        full_name=user.full_name,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def remove_all_users(db: Session):
    db.query(models.User).delete()
    db.commit()