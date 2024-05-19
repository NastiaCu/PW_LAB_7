from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    role = Column(String, default="user")
    calorie_logs = relationship("CalorieLog", back_populates="user")

class CalorieLog(Base):
    __tablename__ = 'calorie_logs'
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    food_item = Column(String, index=True)
    calories = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="calorie_logs")