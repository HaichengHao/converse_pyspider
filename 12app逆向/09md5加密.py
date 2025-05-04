"""
@File    :09md5加密.py
@Editor  : 百年
@Date    :2025/5/4 9:11 
"""
'''
- `hexdigest()`返回的是一个十六进制字符串，不能直接解码回字符字符串。
   - `digest()`返回的是字节对象，可以直接处理为二进制数据。'''


import hashlib

obj = hashlib.md5()
obj.update('abcdefg'.encode('utf-8'))

v1 = obj.hexdigest()
print(v1)

v2 = obj.digest() #得到的是加密之后的字节 hexdigest本质上是将这些字节转换成16进制的字符串并拼接起来
print(v2)

'''
7ac66c0f148de9519b8bd264312c4d64
b'z\xc6l\x0f\x14\x8d\xe9Q\x9b\x8b\xd2d1,Md
'''

obj0 = hashlib.md5()
obj0.update('要加密的数据'.encode('utf-8'))
v0 = obj0.hexdigest()
print(v0)
# 23e6ba18f30afe82186ab378869656fe
# important:加盐
obj1 = hashlib.md5('abcd123'.encode('utf-8')) # tips:在正式加密要加密的数据之前先传入一个字串用来加密
obj1.update('要加密的数据'.encode('utf-8'))
v2 = obj1.hexdigest()
print(v2)
# ae57c6bbb8bab255419c0d634569fecd 可以看到加盐和不加盐输出的十六进制加密数据得到的结果是不一样的

# md5加密得到的数据一般是32位  2^5 = 32
