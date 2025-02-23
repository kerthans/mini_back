from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db  # 从database.py中导入get_db函数
from utils.database import add_clean_record, get_clean_records  # 导入数据库操作函数
from pydantic import BaseModel
from flask import jsonify, request
from . import api_v1

# 创建 FastAPI 路由器
router = APIRouter()

# 请求体模型 - 用于POST请求，包含"name"和"userid"
class AddCleanRequest(BaseModel):
    name: str
    userid: str

# 响应模型 - 用于统一结构化响应
class CleanResponse(BaseModel):
    code: int
    status: str
    message: str
    data: dict

# POST /api/clean/add - 添加打扫记录
@router.post("/add", response_model=CleanResponse)
def add_clean(request: AddCleanRequest, db: Session = Depends(get_db)):
    try:
        response = add_clean_record(db, name=request.name, userid=request.userid)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="服务器内部错误")

# GET /api/clean/list - 获取打扫记录列表
class GetCleanRequest(BaseModel):
    page: int
    size: int

@router.get("/list", response_model=CleanResponse)
def get_clean(request: GetCleanRequest, db: Session = Depends(get_db)):
    try:
        response = get_clean_records(db, page=request.page, size=request.size)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="服务器内部错误")

