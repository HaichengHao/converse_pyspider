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
#AES


'''
长度:
16:AES-128
24:AES-192
32:AES-256
'''
#导入包 Cipher里边是各种加密器
from Crypto.Cipher import AES

#step1:创建加密器
aes = AES.new(key=b'0123456789abcdef')




