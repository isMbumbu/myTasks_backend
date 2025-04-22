# models.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLAlchemyEnum, Interval
from sqlalchemy.orm import relationship, declarative_base
from enum import Enum
from datetime import datetime, timedelta

Base = declarative_base()

class ImportanceLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("TaskDB", back_populates="user")


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    duration = Column(Interval, nullable=True)
    importance = Column(SQLAlchemyEnum(ImportanceLevel), default=ImportanceLevel.medium)
    expected_finish = Column(DateTime, nullable=True)
    done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("UserDB", back_populates="tasks")
