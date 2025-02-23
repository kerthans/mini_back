from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, SmallInteger # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from datatime import datatime # type: ignore
from . import BaseModel

class StuffBorrow(BaseModel):
    __tablename__ = "stuff_borrow"

    id = Column(Integer, primary_key=True, autotincrement=True)   # 借用记录的唯一标识符，自增主键
    userid = Column(String(50), unique=True)                      # 用户的邮箱账号，唯一认证ID
    sb_id = Column(String(20))                                    # 借物编号
    name = Column(String(50),nullable=False)                      # 借用人姓名
    phone_num = Column(String(11))                                # 借用人手机号码，必须为11位有效号码
    email = Column(String(50))                                    # 借用人邮箱地址
    grade = Column(String(10))                                    # 借用人年级
    major = Column(String(50))                                    # 借用人专业
    project_num = Column(String)                                  # 学校给项目的编号
    mentor_name = Column(String(50), nullable=True)               # 指导老师姓名
    mentor_phone_num = Column(String(11), nullable=True)          # 指导老师电话
    type = Column(String(50),nullable=False)                      # 借用物品的类型
    stuff_name = Column(String(100),nullable=False)               # 具体借用物品的名称
    stuff_quantity_change = Column(Integer,default=0)             # 物品数量的变化，负数表示借出，正数表示增加，0表示未变
    deadline = Column(DateTime,nullable=False)                    # 归还截止时间
    reason = Column(Text)                                         # 新增文本类型字段
    categories = Column(Integer,default=0)                                  # 0表示个人借用，1表示团队借用
    state = Column(Integer,default=0)                             # 0表示未审核，1表示审核通过，2表示审核失败

    def __init__(self,userid,sb_id,name,phone_num,email,grade,major,project_num,mentor_name,mentor_phone_num,type,stuff_name,reason,
    stuff_quantity_change=0,deadline=None,categories=0,state=0):
        self.userid = userid
        self.sb_id = sb_id
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.grade = grade
        self.major = major
        self.project_num = project_num
        self.mentor_name = mentor_name
        self.mentor_phone_num = mentor_phone_num
        self.type = type
        self.stuff_name = stuff_name
        self.reason = reason
        self.stuff_quantity_change = stuff_quantity_change
        self.categories = categories
        self.state = state
        self.deadline = deadline if deadline else datatime.now().isoformat() # 默认截止时间为当前时间，用 ISO 8601 格式


