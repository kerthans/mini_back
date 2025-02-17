from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.database import engine, Base
from api_routes.v1 import users, rules, events, tasks, projects

# 创建所有数据表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Makers管理系统API",
    description="四川大学创客空间管理系统后端API",
    version="1.0.0"
)

# CORS设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(rules.router, prefix="/api/v1", tags=["rules"])
app.include_router(events.router, prefix="/api/v1", tags=["events"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(projects.router, prefix="/api/v1", tags=["projects"])

@app.get("/")
async def root():
    return {"message": "Welcome to Makers Management System API"}
