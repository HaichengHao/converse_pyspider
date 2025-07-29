"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/7/28 14:24 
"""
from flask import Flask
import settings
app = Flask(__name__)
app.config.from_pyfile('settings.py')

#tips:也可以这样
app.config.from_object(settings)

# tips:也可以这样设置
app.config['ENV'] = 'development'

@app.route('/index')
def index():
    app.run(debug=True,host='0.0.0.0',port=8080)

#summary : 新增三种方式,一种是解耦,放到settings文件当中进行导入,另一种是直接指定键来修改值,还有一种是直接导入.py