"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/4 14:16 
"""
from bpproject import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host='127.0.0.1',port=8090)

