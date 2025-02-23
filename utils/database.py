from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from datetime import datetime
import uuid
from models.arrange import Arrange  # 引入 Clean 模型
from models.message import Message
from sqlalchemy.orm import Session

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
print(os.getenv("DATABASE_URL"))

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# 添加安排记录
def add_arrange_record(db: Session, name: str, type: str, order: int):
    new_arrange = Arrange(name=name, type=type, order=order)
    db.add(new_arrange)
    db.commit()
    db.refresh(new_arrange)
    return new_arrange

# 学年活动记录表
# 获取所有安排记录
def get_arrange_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Arrange).offset(skip).limit(limit).all()

# 获取某个安排记录
def get_arrange_by_id(db: Session, arrange_id: int):
    return db.query(Arrange).filter(Arrange.id == arrange_id).first()

# 更新安排记录
def update_arrange_record(db: Session, arrange_id: int, name: str, type: str, order: int):
    arrange = db.query(Arrange).filter(Arrange.id == arrange_id).first()
    if arrange:
        arrange.name = name
        arrange.type = type
        arrange.order = order
        db.commit()
        db.refresh(arrange)
        return arrange
    return None

# 删除安排记录
def delete_arrange_record(db: Session, arrange_id: int):
    arrange = db.query(Arrange).filter(Arrange.id == arrange_id).first()
    if arrange:
        db.delete(arrange)
        db.commit()
        return True
    return False


# 信息表
# 添加消息记录
def add_message_record(db: Session, message_id: str, sender_id: str, receiver_id: str, content: str, time_stamp: str, state: int):
    new_message = Message(message_id=message_id, sender_id=sender_id, receiver_id=receiver_id, content=content, time_stamp=time_stamp, state=state)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

# 获取所有消息记录
def get_message_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Message).offset(skip).limit(limit).all()

# 获取某个消息记录
def get_message_by_id(db: Session, message_id: int):
    return db.query(Message).filter(Message.id == message_id).first()

# 更新消息记录
def update_message_record(db: Session, message_id: int, content: str, state: int):
    message = db.query(Message).filter(Message.id == message_id).first()
    if message:
        message.content = content
        message.state = state
        db.commit()
        db.refresh(message)
        return message
    return None

# 删除消息记录
def delete_message_record(db: Session, message_id: int):
    message = db.query(Message).filter(Message.id == message_id).first()
    if message:
        db.delete(message)
        db.commit()
        return True
    return False


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



