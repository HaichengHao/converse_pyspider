"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/3 9:57 
"""


from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html',msg='hello world ')
#自定义一个过滤器,实现检测到'hello'就替换
def replace_hello(v):
    if 'hello' in v:
        va = v.replace('hello','你好').strip()
        return va
#然后加入模板过滤器
app.add_template_filter(replace_hello,'repl')


#tips:还有一种方式,利用装饰器
lst = [0,1,2,3,4,5]
@app.route('/srl')
def srl():
    return render_template('srl.html',msg=lst)

@app.template_filter('revlst')
def rev_lst(lst):
    lst = list(lst)
    lst.reverse()
    return lst




if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=8080)

