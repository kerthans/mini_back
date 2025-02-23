from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel, EmailStr

Base = declarative_base()

class DutyApply(Base):
        __tablename__ = 'duty_apply'

        id = Column(Integer, primary_key=True)
        apply_id = Column(String, unique=True)
        name = Column(String)
        userid = Column(String)
        day = Column(String)
        time_section = Column(Integer)
        created_at = Column(String)

#定义post所需的一系列模型
#定义请求模型
class PostProductRequest(BaseModel):
    apply_id:str
    userid:str
    name:str
    day:str
    time_section:int
    created_at:str

# 定义嵌套的 Data 模型
class Data(BaseModel):
    apply_id: str

#定义响应的主模型
class PostProductResponse(BaseModel):
    code: int
    status: str
    message: str
    data:Data
#定义综合响应模型
class PostOKResponseWithProduct(PostProductResponse):
    pass

#定义get所需的一系列模型
#定义响应的嵌套模型
class GetData(BaseModel):
    apply_id: str
    userid: str
    name: str
    day: str
    time_section: int
    created_at: str
# 定义响应的主模型
class GetProductResponse(BaseModel):
    code: int
    status: str
    data:GetData
#定义综合响应模型
class GetOKResponseWithProduct(GetProductResponse):
    pass

#定义delete所需的一系列模型
#定义响应的主模型
class DeleteProductResponse(BaseModel):
    code: int
    status: str
    message: str
    data: Data  #与上文post响应模型中的嵌套模型一致
# 定义综合响应模型
class DeleteOKResponseWithProduct(DeleteProductResponse):
    pass
