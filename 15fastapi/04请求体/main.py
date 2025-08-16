"""
@File    :main.py
@Editor  : 百年
@Date    :2025/8/14 15:27 
"""
from apps import create_app
import uvicorn
app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True,host='127.0.0.1',port=8099)

