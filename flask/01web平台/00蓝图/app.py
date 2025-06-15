"""
@File    :app.py
@Editor  : 百年
@Date    :2025/6/15 10:48 
"""
from myproject import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
