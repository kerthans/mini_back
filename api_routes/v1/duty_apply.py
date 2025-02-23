from fastapi import FastAPI, HTTPException, Depends
from .database import get_db, SessionLocal
from .models import User
from .schemas import UserCreate, UserResponse
from sqlalchemy.orm import Session

app = FastAPI()

#api路由
#post
@app.post("/duty_apply/",response_model=PostOKResponseWithProduct)
async def post_product(request: PostProductRequest, db: Session = Depends(get_db)):
    existing_data = db.query(DutyApply).filter(DutyApply.apply_id == request.apply_id).first()
    if(existing_data):
        response={
        "code": 200,
        "status": "success",
        "message": "申请提交成功",
        "data": {
            "apply_id": DutyApply.apply_id
                }
            }

    return response

@app.get("/",response_model=GetOKResponseWithProduct)
async def get_product():
    response={
        {
            "code": 200,
            "status": "success",
            "data": {
                "apply_id":DutyApply.apply_id,
               "userid":DutyApply.userid,
                "name":DutyApply.name,
                "day":DutyApply.day,
                "time_section":DutyApply.time_section,
                "created_at":DutyApply.created_at

            }

    }

    }
    return response

@app.delete("/duty_apply/id/",response_model=DeleteOKResponseWithProduct)
async def delete_product(id:str):
    response={
        "code": 200,
        "status": "success",
        "message": "申请删除成功",
        "data": {
        "apply_id":DutyApply.apply_id
    }
    }
