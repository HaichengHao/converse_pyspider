# @Author    : 百年
# @FileName  :04基于文件进行授权.py
# @DateTime  :2024/10/28 9:22
'''
如果是私有服务，那就用这个，这样给钱的才能用你的API，否则不能使用
'''
import hashlib
from flask import Flask, jsonify, request

# 创建app对象
app = Flask(__name__)


# 定义一个函数用来验证token的合法性
def get_user_dict():
    info_dic = {}  # 创建一个字典用于接收一会儿返回的字符串
    with open('db.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.strip()
            token, name = line.split(',')  # 根据逗号来切分，返回的是个列表
            info_dic[token] = name
    return info_dic


@app.route('/bili', methods=['POST', 'GET'])
def bili():
    '''
    请求的数据格式要求的是字典
    假设凭证关系存储在db.txt中，我们用uuid.uuid4()生成数字凭证
    要求请求的url中需要携带token(令牌)
    例如/bili?token=uuid,如果是已经有的uuid,那么就返回API，否则不返回
    '''
    # 注意token是url携带的，所以要用args.get获取的方式
    token = request.args.get("token")  # 先获取token
    if not token:  # 如果未携带token,则直接返回认证失败
        return jsonify({"status": False, "error": "认证失败,请联系管理员获取token"})

    # 如果携带了token,则需要验证token的合法性
    # 调用我们写的函数验证token
    user_dict = get_user_dict()  # 通过这一步拿到所有我们知道的token
    if token not in user_dict:  # 如果携带token但是该token不合法
        return jsonify({"status": False, "error": "认证失败,令牌错误"})

    # 如果在就正常的往后进行
    ordered_string = request.json.get("ordered_string")
    if not ordered_string:  # 如果没有得到ordered_string
        return jsonify({"status": False, "error": "参数错误"})
    # 如果获取到了就调用核心sign
    encrypt_string = ordered_string + "560c52ccd288fed045859ed18bffd973"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign = obj.hexdigest()
    # 将签名的结果返回给用户
    return jsonify({"status": True, "data": sign})


if __name__ == '__main__':
    app.run()
