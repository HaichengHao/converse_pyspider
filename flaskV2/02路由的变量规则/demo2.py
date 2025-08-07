"""
@File    :demo2.py
@Editor  : 百年
@Date    :2025/8/3 20:01 
"""
#important:本文件是对于遗漏的url_for的补充
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '首页'


@app.route('/user/<username>')
def user_profile(username):
    return f'用户 {username} 的个人资料'


with app.test_request_context():
    # 生成首页的 URL
    print(url_for('index'))  # 输出: /

    # 生成带参数的 URL
    print(url_for('user_profile', username='张三'))  # 输出: /user/张三

'''
在 Jinja2 模板中同样可以使用 url_for()：
<a href="{{ url_for('index') }}">首页</a>
<a href="{{ url_for('user_profile', username='张三') }}">张三的资料</a>

'''

# url_for() 可以自动处理查询参数，只需在函数中传入额外的关键字参数：
@app.route('/search')
def search():
    return '搜索结果'

with app.test_request_context():
    # 生成带查询参数的 URL
    print(url_for('search', q='flask', page=2))  # 输出: /search?q=flask&page=2


# 对于 CSS、JavaScript、图片等静态文件，Flask 提供了特殊的 static 端点：
# 生成静态文件的 URL
url_for('static', filename='css/style.css')  # 输出: /static/css/style.css

# 在模板中引用静态文件：
# <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">


# 如果在蓝图中定义路由，需要指定蓝图名称作为前缀：
# admin.py 蓝图
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
def dashboard():
    return '管理员面板'

# 在生成 URL 时需要指定蓝图名称
url_for('admin.dashboard')  # 输出: /admin/dashboard (假设蓝图的 url_prefix 是 /admin)


'''

为什么使用 url_for() 而不是硬编码 URL？
维护性：当路由的 URL 发生变化时，只需修改 @app.route() 中的定义，所有通过 url_for() 生成的 URL 会自动更新。
灵活性：自动处理 URL 编码、查询参数拼接等细节。
一致性：确保所有 URL 遵循统一的路由规则，避免拼写错误。

总之，url_for() 是 Flask 中推荐的生成 URL 的方式，尤其在大型应用中能显著提高代码的可维护性。
'''