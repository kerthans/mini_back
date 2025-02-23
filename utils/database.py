from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv  
from typing import List, Optional, Dict  # 导入 List、Optional 和 Dict
import os


load_dotenv()


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 定义 Task 表模型
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task_id = Column(String(255), unique=True) 
    department = Column(String(100)) 
    task_name = Column(String(255)) 
    name = Column(String(100))  
    content = Column(Text)
    state = Column(Integer, default=0)
    deadline = Column(String(50))
#定义物资表模型
class Stuff(Base):
    __tablename__ = 'stuff'

    id = Column(Integer, primary_key=True)
    stuff_id = Column(String(255), unique=True)  
    type = Column(String(100)) 
    stuff_name = Column(String(255))   
    number = Column(Integer)
    description = Column(Text)
    created_at = Column(String(50))  
    updated_at = Column(String(50))  
#定义借物表模型
class StuffBorrow(Base):
    __tablename__ = 'stuff_borrow'

    id = Column(Integer, primary_key=True)
    sb_id = Column(String(255), unique=True) 
    userid = Column(String(100))  
    name = Column(String(100)) 
    phone_num = Column(String(50)) 
    email = Column(String(255)) 
    grade = Column(String(50))  
    major = Column(String(100)) 
    project_num = Column(String(100)) 
    type = Column(String(100)) 
    stuff_name = Column(String(255))  
    stuff_quantity_change = Column(Integer) 
    deadline = Column(String(50))
    reason = Column(Text)
    categories = Column(Integer, default=0)
    state = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)



# Task 表的 CRUD 操作
def create_task(
    db: Session, 
    task_id: str, 
    department: str, 
    task_name: str, 
    name: str, 
    content: str, 
    state: int, 
    deadline: str
) -> Task:
    """
    创建新任务
    """
    db_task = Task(
        task_id=task_id,
        department=department,
        task_name=task_name,
        name=name,
        content=content,
        state=state,
        deadline=deadline
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(
    db: Session, 
    skip: int = 0, 
    limit: int = 10
) -> List[Task]:
    """
    获取任务列表，支持分页
    """
    return db.query(Task).offset(skip).limit(limit).all()

def update_task(
    db: Session, 
    task_id: str, 
    update_data: Dict[str, Optional[str | int]]
) -> Optional[Task]:
    """
    更新任务字段
    """
    db_task = db.query(Task).filter(Task.task_id == task_id).first()
    if not db_task:
        return None
    
    # 更新字段
    for key, value in update_data.items():
        if hasattr(db_task, key) and value is not None:
            setattr(db_task, key, value)
    
    # 提交事务
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: str) -> bool:
    """
    删除任务
    """
    db_task = db.query(Task).filter(Task.task_id == task_id).first()
    if not db_task:
        return False
    
    # 删除记录
    db.delete(db_task)
    db.commit()
    return True

# Stuff 表的 CRUD 操作
def create_stuff(
    db: Session, 
    stuff_id: str, 
    type: str, 
    stuff_name: str, 
    number: int, 
    description: str, 
    created_at: str, 
    updated_at: str
) -> Stuff:
    """
    创建物资
    """
    db_stuff = Stuff(
        stuff_id=stuff_id,
        type=type,
        stuff_name=stuff_name,
        number=number,
        description=description,
        created_at=created_at,
        updated_at=updated_at
    )
    db.add(db_stuff)
    db.commit()
    db.refresh(db_stuff)
    return db_stuff

def get_stuff(
    db: Session, 
    skip: int = 0, 
    limit: int = 10
) -> List[Stuff]:
    """
    获取物资列表，支持分页
    """
    return db.query(Stuff).offset(skip).limit(limit).all()

def update_stuff(
    db: Session, 
    stuff_id: str, 
    update_data: Dict[str, Optional[str | int]]
) -> Optional[Stuff]:
    """
    更新物资字段
    """
    db_stuff = db.query(Stuff).filter(Stuff.stuff_id == stuff_id).first()
    if not db_stuff:
        return None
    
    # 更新字段
    for key, value in update_data.items():
        if hasattr(db_stuff, key) and value is not None:
            setattr(db_stuff, key, value)
    
    # 提交事务
    db.commit()
    db.refresh(db_stuff)
    return db_stuff

def delete_stuff(db: Session, stuff_id: str) -> bool:
    """
    删除物资
    """
    db_stuff = db.query(Stuff).filter(Stuff.stuff_id == stuff_id).first()
    if not db_stuff:
        return False
    
    # 删除记录
    db.delete(db_stuff)
    db.commit()
    return True

# StuffBorrow 表的 CRUD 操作
def create_stuff_borrow(
    db: Session, 
    sb_id: str, 
    userid: str, 
    name: str, 
    phone_num: str, 
    email: str, 
    grade: str, 
    major: str, 
    project_num: str, 
    type: str, 
    stuff_name: str, 
    stuff_quantity_change: int, 
    deadline: str, 
    reason: str, 
    categories: int, 
    state: int
) -> StuffBorrow:
    """
    创建物品借用记录
    """
    db_stuff_borrow = StuffBorrow(
        sb_id=sb_id,
        userid=userid,
        name=name,
        phone_num=phone_num,
        email=email,
        grade=grade,
        major=major,
        project_num=project_num,
        type=type,
        stuff_name=stuff_name,
        stuff_quantity_change=stuff_quantity_change,
        deadline=deadline,
        reason=reason,
        categories=categories,
        state=state
    )
    db.add(db_stuff_borrow)
    db.commit()
    db.refresh(db_stuff_borrow)
    return db_stuff_borrow

def get_stuff_borrow(
    db: Session, 
    skip: int = 0, 
    limit: int = 10
) -> List[StuffBorrow]:
    """
    获取物品借用记录列表，支持分页
    """
    return db.query(StuffBorrow).offset(skip).limit(limit).all()

def update_stuff_borrow(
    db: Session, 
    sb_id: str, 
    update_data: Dict[str, Optional[str | int]]
) -> Optional[StuffBorrow]:
    """
    更新物品借用记录字段
    """
    db_stuff_borrow = db.query(StuffBorrow).filter(StuffBorrow.sb_id == sb_id).first()
    if not db_stuff_borrow:
        return None
    
    # 更新字段
    for key, value in update_data.items():
        if hasattr(db_stuff_borrow, key) and value is not None:
            setattr(db_stuff_borrow, key, value)
    
    # 提交事务
    db.commit()
    db.refresh(db_stuff_borrow)
    return db_stuff_borrow

def delete_stuff_borrow(db: Session, sb_id: str) -> bool:
    """
    删除物品借用记录
    """
    db_stuff_borrow = db.query(StuffBorrow).filter(StuffBorrow.sb_id == sb_id).first()
    if not db_stuff_borrow:
        return False
    
    # 删除记录
    db.delete(db_stuff_borrow)
    db.commit()
    return True


