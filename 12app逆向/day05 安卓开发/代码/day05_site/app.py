import flask

from flask import Flask, request, jsonify

app = Flask(__name__)


# http://192.168.0.6:9999/login
# user=xxx
# pwd=xx
# sign=xx
@app.route('/login', methods=["POST"])
def login():
    # 1.接收请求数据
    print(request.form)

    # 2.校验签名

    # 3.校验用户名和密码是否正确

    # 4.返回值
    return jsonify({"status": True, 'token': "dafkauekjsoiuksjdfuxdf"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999)
