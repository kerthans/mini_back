from sqlalchemy import Column, Integer, String, Text, LargeBinary
from sqlalchemy.orm import declarative_base
from .base import BaseModel
from datetime import datetime

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    # 字段定义
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(String(50), unique=True, index=True)  # 活动唯一ID
    event_name = Column(String(255), nullable=False)
    poster = Column(LargeBinary, nullable=False)  # Base64图片数据（非空）
    description = Column(Text, nullable=False)
    location = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    start_time = Column(String(50), nullable=False)  # ISO 8601开始时间
    end_time = Column(String(50), nullable=False)  # ISO 8601结束时间
    registration_deadline = Column(String(50), nullable=False)
    created_at = Column(String(50), nullable=False)
    updated_at = Column(String(50), nullable=False)

    # 初始化方法
    def __init__(self,event_id = None,event_name= None,poster= None,description = None,location= None,link = None,
                 start_time = None,end_time = None,registration_deadline = None, created_at = None,updated_at = None):

        timestamp = datetime.now().isoformat() + 'Z'

        self.event_id = event_id 
        self.event_name = event_name
        self.poster = poster
        self.description = description
        self.location = location
        self.link = link
        self.start_time = start_time
        self.end_time = end_time
        self.registration_deadline = registration_deadline
        self.created_at = created_at or timestamp
        self.updated_at = updated_at or timestamp




# Pydantic模型
class BaseSchema(BaseModel):
    id: int
    created_at: datetime
class EventSchema(BaseSchema):
    event_id: str
    event_name: str
    poster: bytes  # Base64 编码后的图片数据，使用 bytes 存储
    description: str
    location: str
    link: str
    start_time: str  # ISO 8601 格式时间，必要时可改为 datetime
    end_time: str    # ISO 8601 格式时间
    registration_deadline: str  # 报名截止时间
    updated_at: str  # 最后更新时间



