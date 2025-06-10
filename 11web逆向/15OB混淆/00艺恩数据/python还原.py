"""
@File    :python还原.py
@Editor  : 百年
@Date    :2025/6/7 18:48 
"""
import json
import requests
import binascii
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import requests


def get_data():
    url = 'https://www.endata.com.cn/API/GetData.ashx'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }

    data = {
        "year": "2025",
        "MethodName": "BoxOffice_GetYearInfoData"
    }

    response = requests.post(url=url, headers=headers, data=data)
    print(response.text)

    # 得到data数据
    data = response.text
    return data


# def shell(s):
#     a = int(s[-1],16)+9
#     b = int(s[a],16)
#     return a,b

def subfunc(a, param1, param2):
    if param1 == 0:
        return a[param2:]

    data = str(a[:param1])
    data += a[param1 + param2:]
    return data


# 准备进行数据的解密逻辑
def decrypt_data(s):
    a = int(s[-1], 16) + 9
    print(a)
    b = int(s[a], 16)
    print(b)
    s = subfunc(s, a, 1)
    print(s)
    a = s[b: b+8]
    print(a)
    data = subfunc(s, b, 8)  # 注意这时候的data是16进制的字符串
    print(data)
    key = a.encode('utf-8')
    print(key)
    iv = a.encode('utf-8')

    # 将data转换为字节
    bs = binascii.a2b_hex(data)
    des = DES.new(key=key, mode=DES.MODE_ECB)  # 注意看还原的js代码,key和iv是一样的,所以不用给了,而且是ECB模式,没有初始向量iv
    des_dara = des.decrypt(bs)
    des_dara = unpad(des_dara,8)
    return des_dara.decode('utf-8')


if __name__ == '__main__':
    data_source = get_data()
    print(type(data_source))
    result = decrypt_data(data_source)
    # print(result)

    #但是如果想转化为json数据就得把后面的日期去掉
    last_brace_pose = result.rfind('}')
    if last_brace_pose !=-1: #即若不是最后以}结尾
        json_data = result[:last_brace_pose + 1]
        final_optimized = json.loads(json_data)
        print(final_optimized['Data']['Table'])



    # print(unpad(result,8))
