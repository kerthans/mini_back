from .error_handler import init_error_handlers

def init_middleware(app):
    """初始化所有中间件"""
    init_error_handlers(app)
