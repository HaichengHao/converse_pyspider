"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/8/6 16:51 
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
