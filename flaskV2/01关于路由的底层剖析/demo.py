"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/29 8:25 
"""
from flask import Flask
import settings
app = Flask(__name__)
app.config.from_object(settings)
#tips: 我们写路由一般都是这样写的

'''
@app.route('/index')
def index():
    pass
'''
#tips:可以看看route的底层实现,其实它就相当于

def index():
    return 'hello'


app.add_url_rule('/index',view_func=index)

if __name__ == '__main__':
    app.run()