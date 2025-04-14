"""
@File    :00md5加密.py
@Editor  : 百年
@Date    :2025/3/29 18:56 
"""
import hashlib
pwd = '123456'
obj = hashlib.md5(pwd.encode('utf-8'))
sign = obj.hexdigest()
print(sign)