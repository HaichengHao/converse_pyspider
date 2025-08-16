"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/8/8 19:57 
"""
from apps import create_app
from apps.user.models import User
app = create_app()

if __name__ == '__main__':
    app.run()