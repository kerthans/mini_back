# mini_back

Makers小程序后端

API文档：

https://xi1uh4zvhbc.feishu.cn/docx/AgqldIq1No5WdWx83zOcJJH9nSf?from=from_copylink

```
├── app/
│   ├── __init__.py          # 包初始化
│   ├── app.py              # FastAPI 应用主文件
│   ├── models/              # 数据库模型
│   │   ├── __init__.py
│   │   ├── role.py          # 角色表模型
│   │   ├── user.py          # 用户表模型
│   │   ├── task.py          # 任务表模型
│   │   └── 其他模型文件
│   ├── crud/                # CRUD 操作
│   ├── index/               # 请求和响应数据验证（Pydantic）
│   ├── api/                 # API 路由
│   │   ├── __init__.py
│   │   ├── roles.py         # 角色相关 API
│   │   ├── users.py         # 用户相关 API
│   │   ├── tasks.py         # 任务相关 API
│   │   └── 其他表的路由文件
│   ├── services/            # 业务逻辑处理
│   └── utils/               # 工具类
├── requirements.txt         # Python 依赖
├── .env                     # 环境变量配置文件
└── README.md                # 项目说明文档
```