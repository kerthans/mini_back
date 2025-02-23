from sqlalchemy import Column, Integer, String, LONGBLOB, Text
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .models import BaseModel

# SQLAlchemy Base
Base = declarative_base()

# SQLAlchemy User 模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String, unique=True, index=True)
    password = Column(String)
    level = Column(Integer, default=1)
    realname = Column(String)
    phone_num = Column(String, default="")
    note = Column(Text, default="暂无")
    state = Column(Integer, default=1)
    profile_photo = Column(LONGBLOB, default=None)
    score = Column(Integer, default=0)

# Pydantic Userbase
class Userbase(BaseModel):
    userid: str
    password: str
    level: int = 1
    realname: str
    phone_num: str = ""
    note: str = "暂无"
    state: int = 1
    profile_photo: Optional[bytes] = None
    score: int = 0

class UserSchema(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
    

