"""
@File    :app.py
@Editor  : 百年
@Date    :2025/6/23 19:37 
"""
from myweb_optimize import create_app
# 创建app对象

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
