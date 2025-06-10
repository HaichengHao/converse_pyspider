"""
@File    :12rsa解密当乐网.py
@Editor  : 百年
@Date    :2025/6/4 16:14 
"""
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
import binascii
e = '10001'
n='be44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd'


decimal_e = int(e,16)
decimal_n = int(n,16)
print(decimal_e)
print(decimal_n)  #这样就得到了十进制的n

#然后走数学结构的加密逻辑

#接下来就是明文,这里假设密码是123456abc
pwd = '123456'[::-1]    #important:最终算出来后发现刚好是倒过来的,那就在传入的时候倒着传入
#important:但是这玩意是个字符串,需要将其转换成整数,需要使用之前学的binascii

# 将字节转化为16进制,传入的是字节,所以要把pwd做encode转换成字节形式
pwd = binascii.b2a_hex(pwd.encode('utf-8'))
print(pwd)
print(int(pwd.decode(),16))  #这里打印转换成10进制试试看

encpwd = int(pwd.decode(),16)**decimal_e % decimal_n
print('加密后的密文:\n',encpwd)

#再将其转换为16进制
hex_pwd = hex(encpwd).replace('0x',"")
print(f'最终:{hex_pwd}')