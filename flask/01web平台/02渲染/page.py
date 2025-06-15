"""
@File    :page.py
@Editor  : 百年
@Date    :2025/6/15 13:22 
"""
from flask import Flask, render_template
import pymysql

conn = pymysql.Connection(
    host='localhost',
    port=3306,
    user='root',
    password='HHCzio20',
    # charset='utf-8',
    database='flaskdemo',
    cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)


def db_opt_dml(sql, *paramas):
    cursor = conn.cursor()
    cursor.execute(sql, *(paramas))
    result = cursor.fetchone()
    print(result)
    cursor.close()
    return result


def dp_opt_dql(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


@app.route('/getinfo')
def getinfo():
    info = dp_opt_dql(sql='select * from user_info')
    print(info)
    # for item in info:
    return render_template('getinfo.html',items = info)


# 先写一个用来测试一下试试
@app.route('/demo')
def demo():
    context = {'n1': '张三',
               'n2': 256,
               'n3': [11, 22, 33, 44]}
    v4 = {'name': '赵子龙', 'age': 23}
    v5 = [
        {'name': '张飞', 'age': 32},
        {'name': '刘备', 'age': 36}
    ]

    return render_template('demo.html', **context,n4=v4,n5=v5)


if __name__ == '__main__':
    app.run(debug=True)
