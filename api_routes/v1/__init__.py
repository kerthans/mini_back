# 初始化 models 模块

from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

# 导入所有路由模块
from . import (
    users, rules, events, tasks,
    stuff_borrow, stuff, SiteBorrow,
    projects, Games, honor,
    DutyRecord, DutyApply, Clean,
    Arrange, PubliityLink, Messages
)

