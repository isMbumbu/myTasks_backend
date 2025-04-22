# schemas.py

from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
from enum import Enum

class ImportanceLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    user_id: int
    duration: timedelta | None = None
    importance: ImportanceLevel = ImportanceLevel.medium
    expected_finish: datetime | None = None
    done: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
