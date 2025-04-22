from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime, timedelta


class ImportanceLevel(str, Enum):
     low  = "low"
     medium ="medium"
     high= "high"


class UserBase(BaseModel):
    name:str
    email: EmailStr
    password:str

    class Config():
         orm_mode: True


class User(UserBase):
     id: int
     created_at:datetime


class TaskBase(BaseModel):
     user_id:int
     duration: timedelta | None = None
     importance: ImportanceLevel = ImportanceLevel.medium
     expected_finish: datetime | None = None
     done: bool = False

     class Config():
          orm_mode: True

class Task(TaskBase):
     id: int
     created_at:datetime
     
