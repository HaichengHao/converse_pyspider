"""
@File    :05AES.py
@Editor  : 百年
@Date    :2025/5/30 14:29 
"""
'''
pip install pycrypto 
pip install pycryptodome
对称加密
所谓对称加密就是加密和解密用的是同一个密钥
条件:加密和解密用的是同一个密钥,那么两边就必须拥有相同的钥匙才可以打开
常见的对称加密有aes,des,3des（3des）
'''
# AES


'''
长度:
16:AES-128
24:AES-192
32:AES-256
'''
# 导入包 Cipher里边是各种加密器
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# step1:创建加密器
aes = AES.new(key=b'0123456789abcdef', mode=AES.MODE_CBC, iv=b'0123456789123456')
'''
  For ``MODE_CBC``, ``MODE_CFB``, and ``MODE_OFB`` it must be 16 bytes long.'''
'''
MODE_ECB 不需要IV
而MODE_CBC需要IV
IV长度为16
'''

# step2:加密一段数据
s = '你好,世界,hello world'

bs = s.encode('utf-8')  # important:注意传入的是字节
bs = pad(bs, 16)  # 进行填充,如果报错提示填充到8的倍数那就填8
bs = aes.encrypt(bs)
try:
    print(bs)
    # b' A\x84\x9dG\x02\xb5\xb1\xed\xc9\xb5jt\x85T}\xd9\x81{.tG\xf4Ag\xfam\xda\\\xb80\x01'
    # 加密后的结果是杂乱无章的字节
except BaseException as e:
    print(e)
    # ValueError: Data must be padded to 16 byte boundary in CBC mode
    # 数据必须是16的倍数，所以需要填充到16的倍数

# 加密完的字节也是不能够直接发送给服务器的,所以要将字节转换为服务器能够识别的字符串
# 也就用到了base64编码
import base64

res = base64.b64encode(bs).decode()
print(res)
# IEGEnUcCtbHtybVqdIVUfdmBey50R/RBZ/pt2ly4MAE=
