import datetime

from flask import Flask
from Faab.extendsions import db
from Faab.FaabJWT import JWT
from flasgger import Swagger
import inspect
from Faab.FaabFunction import AutoUrl


def get_variable_name(obj):
    # 遍历当前作用域的变量
    frame = inspect.currentframe().f_back
    # 遍历当前帧的变量
    for name, value in frame.f_locals.items():
        if value is obj:
            return name
    return None


def create_app(app, models, db_config, url_prefix='/api/'):
    # Swagger
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = 'AutoFlask'  # 配置大标题
    swagger_config['description'] = 'AutoFlask生成的Swagger文档'  # 配置公共描述内容
    swagger_config['version'] = '1.0.0'  # 配置版本
    Swagger(app, config=swagger_config)

    app.config.from_object(db_config)
    # 注册蓝本
    for model in models:
        AutoUrl(model)
        app.register_blueprint(model[0]["bp"], url_prefix=url_prefix)
    app.register_blueprint(JWT)

    # 初始化扩展
    db.init_app(app)
    with app.app_context():
        # 在应用程序上下文中执行需要应用程序的操作
        # db.drop_all()
        db.create_all()
    return app
