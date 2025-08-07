"""
@File    :app.py
@Editor  : 百年
@Date    :2025/7/31 9:22 
"""
from demoproject import createapp

if __name__ == '__main__':
    app = createapp()
    app.run(debug=True,port=8090,host='127.0.0.1')
