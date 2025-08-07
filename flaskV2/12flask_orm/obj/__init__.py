"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/8/6 10:28 
"""

from flask import Flask
from .exts import db,mig
from settings import devConfig
def create_app():
    app = Flask(__name__)

    app.config.from_object(devConfig)


    #初始化扩展
    db.init_app(app)

    #初始化migrate
    mig.init_app(app=app,db=db)


    @app.cli.command()
    def test_db():
        """测试数据库连接"""

        with app.app_context():
            db.create_all()
        print("数据库表已创建")

    return app