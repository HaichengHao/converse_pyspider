# @Author    : 百年
# @FileName  :app.py
# @DateTime  :2025/7/4 19:08
from demo_file_upload import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=5000,host='127.0.0.1')