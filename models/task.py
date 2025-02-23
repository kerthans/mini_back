from sqlalchemy import Column, Integer, String, ForeignKey, Text
from datetime import datetime
from .base import BaseModel

class Task(BaseModel):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)              # 任务的唯一标识符，自增主键
    task_id = Column(String, ForeignKey('other_tasks.id'), unique=True)     # 关联的任务标识符，外键
    department = Column(String, nullable=False)                             # 负责该任务的部门名称
    task_name = Column(String, nullable=False)                              # 任务的名称
    name = Column(String, nullable=False)                                   # 负责该任务的人员名称
    content = Column(Text, nullable=False)                                  # 任务的详细描述
    state = Column(Integer, default=0)                                      # 任务状态：0-未完成，1-已完成
    deadline = Column(String, nullable=False)                               # 任务的截止日期和时间，ISO 8601 格式，例如“2025-01-31T12:00:00Z”

    def __init__(self, task_id, department, task_name, name, content, state=0, deadline=None):
        self.task_id = task_id
        self.department = department
        self.task_name = task_name
        self.name = name
        self.content = content
        self.state = state
        self.deadline = deadline if deadline else datetime.now().isoformat() + 'Z'  # 默认截止时间为当前时间，ISO 8601 格式