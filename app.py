from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
from typing import List, Union, Annotated
from models import User, UserBase, Task,  TaskBase
from sqlalchemy import create_engine


import os

load_dotenv()

app=FastAPI()

DATABASE_URL= os.getenv("DATABASE_URL")

@app.get("/")
def get_root():
    return { "DB_url": DATABASE_URL}