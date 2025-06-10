"""
@File    :算法还原.py
@Editor  : 百年
@Date    :2025/6/5 16:14 
"""
import json

import requests
import binascii
import random
import base64
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad


def a(num):
    # c = ''
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # for j in range(num):
    #     i = random.randint(0,len(b)-1)  #因为randint(a,b)返回的是闭集[a,b],所以我们要写成len(b)-1
    #     c += b[i]
    # return c
    # 更简单的方法:
    return ''.join(random.sample(b, num))  # 表示在b中随机抽取num个字符,但是返回的是列表,所以利用''.join


def b(x, y):
    c = y.encode('utf-8')
    d = "0102030405060708".encode('utf-8')
    e = x.encode('utf-8')
    # 然后将要进行加密步骤
    aes = AES.new(key=c, iv=d, mode=AES.MODE_CBC)
    # 注意填充
    e = pad(e, 16)
    bs = aes.encrypt(e)
    # 还有转换成base64字符串
    bs = base64.b64encode(bs).decode()
    return bs


def c(n, m, p):  # 这里头走的是数学逻辑!!!!   c(i,e,f)
    # 明文是n,但是注意要翻转
    n = n[::-1]
    # 将转换的16进制数值数据转换为ascii值  tips:这里不了解的话可以去看13各种加密逻辑的13rsa解密当乐网
    n = binascii.b2a_hex(n.encode('utf-8'))
    # 然后再将其转换为10进制
    n = int(n.decode(), 16)

    # 先将用到的参数转换成10进制格式
    m = int(m, 16)
    p = int(p, 16)

    # 然后进行运算
    e_s = n ** m % p

    # 运算之后还要将其转换为16进制
    e_s = hex(e_s).replace('0x', '')
    return e_s


def encrypt(s):
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'
    h = {}
    i = a(16)
    h['encText'] = b(s, g)
    # 二次加密
    h['params'] = b(h['encText'], i)
    h['encSecKey'] = c(i, e, f)
    return h


if __name__ == '__main__':
    musicid = input('请输入歌曲id>>>')
    data = {
        "encodeType": "aac",
        "ids": f"[{musicid}]",
        "level": "exhigh"
    }
    param1 = json.dumps(data)
    print(param1)

    res = encrypt(param1)
    print(res)
    # realdata = {
    #     'params': res['encText'],
    #     'encSecKey': res['encSecKey']
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    resp = requests.post(
        url='https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=54be6221a0cd78a0ab63b907790bb1cf',
        headers=headers,
        data=res
    )
    print(resp.text)

    response_source = resp.text
    dic_page_source = json.loads(response_source)
    musci_url = dic_page_source['data'][0]['url']

    #下载音乐,获取二进制文件.content
    bincontent = requests.get(url=musci_url,headers=headers).content
    with open('./demo.mp4','wb') as mf:
        mf.write(bincontent)
        print('下载成功')
