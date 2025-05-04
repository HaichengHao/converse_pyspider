"""
@File    :10sha256加密.py
@Editor  : 百年
@Date    :2025/5/4 9:49 
"""
# 得到的加密的数据一般是64位8个字节


import hashlib

m = hashlib.sha256()
m.update('要加密的数据'.encode('utf-8'))

v = m.hexdigest()
print(v)

m1 = hashlib.sha256()
m1.update('要加密的数据'.encode('utf-8'))
v1 = m.hexdigest()
print(v1)