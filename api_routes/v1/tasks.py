# /api_routes/tasks.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Task  
from utils.database import get_db
from datetime import datetime

router = APIRouter()

# 添加一条任务
@router.post("/tasks/")
def create_task(department: str, task_name: str, name: str, content: str, deadline: str, db: Session = Depends(get_db)):
    task_id = f"TK{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
    new_task = Task(task_id=task_id, department=department, task_name=task_name, name=name, content=content, deadline=deadline)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
            "code": 200,
            "status": "success",
            "message": "任务创建成功", 
            "data": {"task_id": new_task.task_id}
        }

# 获取特定任务详情
@router.get("/tasks/{task_id}")
def get_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="任务未找到")
    return {
        "code": 200,
        "status": "success",
        "message": "获取任务详情成功",
        "data": {
        "task_id": task.task_id,
        "department": task.department,
        "task_name": task.task_name,
        "name": task.name,
        "content": task.content,
        "deadline": task.deadline,
        "state": task.state
    }}

# 删除指定任务
@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="任务未找到")
    db.delete(task)
    db.commit()
    return {
        "code": 200,
        "status": "success",
        "message": "任务删除成功"}

# 获取某个部门的所有任务
@router.get("/tasks/department/{department}")
def get_tasks_by_department(department: str, page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.department == department)
    if not tasks:
        raise HTTPException(status_code=404, detail="该部门目前暂无任务")
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(Task.state == 1).count()
    tasks = tasks.offset((page - 1) * per_page).limit(per_page).all()
    pending_tasks = total_tasks - completed_tasks
    overdue_tasks = tasks.filter(Task.state == 0, Task.deadline < datetime.now().isoformat()).count()

    tasks_data = [{
        "task_id": task.task_id,
        "task_name": task.task_name,
        "name": task.name,
        "deadline": task.deadline,
        "state": task.state
    } for task in tasks]
    
    return {
        "code": 200,
        "status": "success",
        "message": "获取部门任务成功",
        "data": {
            "department": department,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "current_page": page,
            "page_size": per_page,
            "tasks": tasks_data,
            "statistics": {
                "total": total_tasks,
                "completed": completed_tasks,
                "pending": pending_tasks,
                "overdue": overdue_tasks
            }
        }
    }

# 更新任务状态
@router.put("/tasks/{task_id}/state")
def update_task_status(task_id: str, state: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="任务未找到")
    task.state = state
    db.commit()
    return {
        "code": 200,
        "status": "success",
        "message": "任务状态更新成功", 
        "data": {
        "task_id": task.task_id,
        "state": task.state
    }}

# 获取任务列表，支持分页
@router.get("/tasks/list")
def get_task_list(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    total = db.query(Task).count()
    if total == 0:
        raise HTTPException(status_code=404, detail="暂无任务")

    tasks = db.query(Task).offset((page - 1) * per_page).limit(per_page).all()

    tasks_data = [{
        "task_id": task.task_id,
        "department": task.department,
        "task_name": task.task_name,
        "name": task.name,
        "deadline": task.deadline,
        "state": task.state
    } for task in tasks]
    
    return {
        "code": 200,
        "status": "success",
        "message": "成功获取任务列表",
        "data": {
            "total": total,
            "current_page": page,
            "page_size": per_page,
            "tasks": tasks_data
        }
    }

# 更新任务信息
@router.put("/tasks/{task_id}")
def update_task(task_id: str, department: str = None, task_name: str = None, name: str = None, content: str = None, deadline: str = None, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="任务未找到")
    
    if department is not None:
        task.department = department
    if task_name is not None:
        task.task_name = task_name
    if name is not None:
        task.name = name
    if content is not None:
        task.content = content
    if deadline is not None:
        task.deadline = deadline
    
    db.commit()

    return {
        "code": 200,
        "status": "success",
        "message": "任务更新成功",
        "data": {
            "task_id": task.task_id,
            "department": task.department,
            "task_name": task.task_name,
            "name": task.name,
            "content": task.content,
            "deadline": task.deadline
        }
    }