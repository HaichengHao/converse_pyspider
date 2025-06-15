from flask import Flask
from bp.views.account import account


def create_app():
    app = Flask(__name__)
    app.register_blueprint(account)
    return app
