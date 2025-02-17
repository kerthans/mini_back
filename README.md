# mini_back

Makers小程序后端

API文档：

https://xi1uh4zvhbc.feishu.cn/docx/AgqldIq1No5WdWx83zOcJJH9nSf?from=from_copylink

```
project_root/
├── utils/                      # 工具类
│   ├── __init__.py
│   ├── database.py             # 数据库连接和管理
│   ├── cache.py                # 缓存工具
│   ├── logger.py               # 日志工具
│   ├── security.py             # 安全相关工具（加密、解密）
│   └── validators.py           # 数据验证工具
│
├── scripts/                    # 脚本目录
│   ├── deploy/                 # 部署相关脚本
│   │   ├── init_db.py
│   │   └── setup_env.sh
│   └── maintenance/            # 维护脚本
│       ├── backup_db.py
│       └── cleanup.py
│
│
├── models/                     # 数据模型层
│   ├── __init__.py
│   ├── Base.py                 # 基础模型类
│   ├── Rules.py                # 规章制度模型
│   ├── User.py                 # 用户模型
│   ├── Event.py                # 事件模型
│   ├── Project.py              # 项目模型
│   ├── 3dPrinter.py            # 打印机模型
│   ├── Task.py                 # 任务模型
│   ├── SitesBorrow.py          # 场地借用模型
│   ├── Games.py                # 比赛模型
│   ├── Clean.py                # 打扫模型
│   ├── PublicityLink.py        # 秀米模型
│   ├── Arrange.py              # 排班模型
│   ├── Messages.py             # 消息模型
│   ├── DutyRecord.py           # 值班记录模型
│   ├── DutyApply.py            # 值班申请模型
│   ├── Stuff.py                # 物品模型
│   └── StuffBorrow.py         # 借用记录模型
│
├── api_routes/                 # API 路由(controllers也在其中)
│   ├── __init__.py
│   ├── v1/                     # API v1 版本
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── rules.py
│   │   ├── 3dprint.py
│   │   ├── events.py
│   │   ├── tasks.py
│   │   ├── stuff_borrow.py
│   │   ├── stuff.py
│   │   ├── SiteBorrow.py
│   │   ├── projects.py
│   │   ├── Games.py
│   │   ├── honor.py
│   │   ├── DutyRecord.py
│   │   ├── DutyApply.py
│   │   ├── Clean.py
│   │   ├── Arrange.py
│   │   ├── PubliityLink.py
│   │   └── Messages.py
│   └── middleware/             # 中间件
│       ├── __init__.py
│       └── error_handler.py    # 错误处理（log）
│
├── auth.py                     # 认证相关逻辑
├── app.py                    # 应用入口文件
├── .env                        # 配置环境信息
├── .env.example                # 环境信息示例
├── dockerfile                  # Docker 配置文件
├── readme.md                   # 项目说明文档
├── requirements.txt            # 项目依赖
└── .gitignore                  # Git 忽略配置
```
