# API Routes

该文件夹包含项目的API路由定义。

## 目录结构

```
api_routes/                 # API 路由(controllers也在其中)
├── __init__.py
├── v1/                     # API v1 版本
│   ├── __init__.py
│   ├── users.py
│   ├── rules.py
│   ├── 3dprint.py
│   ├── events.py
│   ├── tasks.py
│   ├── stuff_borrow.py
│   ├── stuff.py
│   ├── SiteBorrow.py
│   ├── projects.py
│   ├── Games.py
│   ├── honor.py
│   ├── DutyRecord.py
│   ├── DutyApply.py
│   ├── Clean.py
│   ├── Arrange.py
│   ├── PubliityLink.py
│   └── Messages.py
└── middleware/             # 中间件
    ├── __init__.py
    └── error_handler.py    # 错误处理（log）
```
