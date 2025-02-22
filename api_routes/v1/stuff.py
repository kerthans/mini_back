# from flask import jsonify, request
# from . import api_v1
#
# @api_v1.route('/stuff', methods=['GET'])
# def get_stuff_list():
#     return jsonify({"message": "Get all stuff"})
#
# @api_v1.route('/stuff/<int:stuff_id>', methods=['GET'])
# def get_stuff(stuff_id):
#     return jsonify({"message": f"Get stuff {stuff_id}"})
#
# @api_v1.route('/stuff', methods=['POST'])
# def add_stuff():
#     data = request.get_json()
#     return jsonify({"message": "Add new stuff", "data": data}), 201
#
# @api_v1.route('/stuff/categories', methods=['GET'])
# def get_stuff_categories():
#     return jsonify({"message": "Get stuff categories"})
#=====================================================================#

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from datetime import datetime
from models.stuff import Stuff
from utils.database import get_db
from  pydantic import BaseModel
from typing import  Optional

router = APIRouter()

#获取物资列表
@router.get("/stuff")
async def get_stuff_list(page: int = 1,size: int = 10,db: Session = Depends(get_db)):
    query = db.query(Stuff)
    total = query.count()
    items = query.offset((page - 1) * size).limit(size).all()

    return {
        "code": 200,
        "status": "success",
        "message": "列表获取成功",
        "data": {
            "total": total,
            "page": page,
            "size": size,
            "items": [{
                "id": item.id,
                "stuff_id": item.stuff_id,
                "type": item.type,
                "stuff_name": item.stuff_name,
                "number": item.number,
                "description": item.description,
                "created_at": item.created_at,
                "updated_at": item.updated_at
            } for item in items]
        }
    }

#获取物资详情*****
@router.get("/stuff/{stuff_id}")
async def get_stuff(stuff_id: str,db: Session = Depends(get_db)):
    item = db.query(Stuff).filter(Stuff.stuff_id == stuff_id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="物资不存在"
        )

    return {
        "code": 200,
        "status": "success",
        "message": f"物资详情获取成功{stuff_id}",
        "data": {
            "id": item.id,
            "stuff_id": item.stuff_id,
            "type": item.type,
            "stuff_name": item.stuff_name,
            "number": item.number,
            "description": item.description,
            "created_at": item.created_at,
            "updated_at": item.updated_at
        }
    }

#创建物资条目 暂时不需要
@router.post("/stuff/add")
async def add_stuff(type: str,stuff_name: str,number: int,description: str,db: Session = Depends(get_db)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")     # 生成唯一ID
    new_stuff = Stuff(
        id = None,
        stuff_id = f"ST{timestamp}",
        type = type,
        stuff_name = stuff_name,
        number = number,
        description = description,
        created_at=datetime.now().isoformat(),
        updated_at=datetime.now().isoformat()
    )
    db.add(new_stuff)
    db.commit()
    db.refresh(new_stuff)
    return {
        "code": 200,
        "status": "success",
        "message": "物资添加成功",
        "data": {
            "stuff_id": new_stuff.stuff_id
        }
    }

#更新物资数量
@router.put("/stuff/update")
async def update_stuff_num(stuff_id: str,number: int,db: Session = Depends(get_db)):
    item = db.query(Stuff).filter(Stuff.stuff_id == stuff_id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="物资不存在"
        )

    item.updated_at = datetime.now().isoformat()
    item.number = number
    db.commit()

    return {
        "code": 200,
        "status": "success",
        "message": "物资信息更新成功",
        "data": {
            "id": item.id,
            "stuff_id": item.stuff_id,
            "type": item.type,
            "stuff_name": item.stuff_name,
            "number": item.number,
            "description": item.description,
            "created_at": item.created_at,
            "updated_at": item.updated_at
        }
    }

#删除物资条目 暂时不需要*********
@router.delete("/stuff/{stuff_id}")
async def delete_stuff(stuff_id: str,db: Session = Depends(get_db)):
    item = db.query(Stuff).filter(Stuff.stuff_id == stuff_id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="物资不存在"
        )
    db.delete(item)
    db.commit()
    return {
        "code": 200,
        "status": "success",
        "message": "物资删除成功"
    }

#获取物资种类
@router.get("/stuff/categories")
async def get_stuff_categories(db: Session = Depends(get_db)):
    categories = db.query(Stuff.type.distinct()).all()
    return {
        "code": 200,
        "status": "success",
        "message": "物资种类获取成功",
        "data": [category[0] for category in categories]
    }

#更改物资条目 暂时不需要
class UpdateStuffRequest(BaseModel):
    type: Optional[str] = None
    stuff_name: Optional[str] = None
    description: Optional[str] = None
@router.put("/stuff/{stuff_id}")
async def update_stuff_info(stuff_id: str,request: UpdateStuffRequest,db: Session = Depends(get_db)):
    item = db.query(Stuff).filter(Stuff.stuff_id == stuff_id).first()

    if request.type is not None:
        item.type = request.type
    if request.stuff_name is not None:
        item.stuff_name = request.stuff_name
    if request.description is not None:
        item.description = request.description

    db.commit()
    db.refresh(item)
    return {
        "code": 200,
        "status": "success",
        "message": "物资信息更新成功",
        "data": {
            "stuff_id": item.stuff_id,
            "updated_at": datetime.now().isoformat()
    }
}
