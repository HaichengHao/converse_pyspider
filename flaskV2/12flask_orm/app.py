"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/6 10:28 
"""

# import sys
# import os
#
# # 将项目根目录（当前文件的父目录）添加到 Python 模块搜索路径
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



#flsk-sqlalchemy 实现orm[对象关系] 映射
#flask-migrate 发布命令的工具
from obj import create_app


app = create_app()

if __name__ == '__main__':

    app.run()
