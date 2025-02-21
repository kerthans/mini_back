from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Stuff(Base):
    def __init__(self, id, stuff_id, type, stuff_name, number, description, created_at, updated_at):
        super().__init__(id)
        self.stuff_id = stuff_id
        self.id = id
        self.type = type
        self.stuff_name = stuff_name
        self.number = number
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    __tablename__ = "stuff"

    id = Column(Integer, primary_key = True, index = True)      #标识符
    stuff_id = Column(String, unique = True, index = True)      #物资编号
    type = Column(String)      # 物资类型（如工具、耗材）
    stuff_name = Column(String)     # 物资名称
    number = Column(Integer, default = 0)     # 库存数量
    description = Column(Text, default = "")    # 物资描述
    created_at = Column(String)     # ISO 8601 格式时间
    updated_at = Column(String)     # ISO 8601 格式时间