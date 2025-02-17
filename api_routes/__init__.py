from flask import Blueprint
from .v1 import api_v1

def init_app(app):
    """初始化所有API路由"""
    app.register_blueprint(api_v1, url_prefix='/api/v1')
