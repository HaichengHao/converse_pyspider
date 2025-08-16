"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/8/10 8:43 
"""
import os
from flask import Flask
from .user.extensions import db, migrate
from .config import configdict
from .user.view import user_bps


def create_app(configname=None):
    app = Flask(__name__, template_folder='../templates')

    configname = configname or os.getenv('FLASK_ENV' or 'default')
    app.config.from_object(configdict[configname])

    db.init_app(app)
    app.register_blueprint(user_bps)
    migrate.init_app(app, db)

    return app
