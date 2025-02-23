from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Clean(Base):
    __tablename__ = 'clean'  # 表名为 'clean'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 自动递增的主键
    record_id = Column(String(50), nullable=False, unique=True)  # 记录编号，唯一
    name = Column(String(100), nullable=False)  # 相关人员名称
    userid = Column(String(100), nullable=False)  # 相关人员的电子邮件地址
    times = Column(Integer, nullable=False)  # 打扫次数
    created_at = Column(String(20), default=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))  # 创建时间
    updated_at = Column(String(20), default=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))  # 更新时间

    def __repr__(self):
        return f"<Clean(id={self.id}, record_id={self.record_id}, name={self.name}, times={self.times})>"


