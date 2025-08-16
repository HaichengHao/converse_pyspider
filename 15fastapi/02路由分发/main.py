"""
@File    :main.py
@Editor  : 百年
@Date    :2025/8/14 8:06 
"""
# from fastapi import FastAPI
# import uvicorn
# from .apps import app01,app02
# app = FastAPI()
# app.include_router()
# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port=8099)

import uvicorn
from apps import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app",host='127.0.0.1',port=8099,log_level='debug',reload=True)

# uvicorn main:app --host 127.0.0.1 --port 8099 --reload --log-level debug 或者通过命令来运行