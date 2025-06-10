"""
@File    :06DES.py
@Editor  : 百年
@Date    :2025/5/31 15:26 
"""
from Crypto.Cipher import DES,DES3 #前端里叫3DES(triple DES)
from Crypto.Util.Padding import pad

#创建,注意key和iv都是8位
des = DES.new(key=b'abcdefjs',mode=DES.MODE_CBC,iv=b'0s23q5q7')

s= '天空好像下雨,the sky seem to be raining'
s =s.encode('utf-8')
s_8times = pad(s,8)
s_enc = des.encrypt(s_8times)
print(s_enc)

#再进行base64编码
import base64

#输出b64字符串
b64s = base64.b64encode(s_enc).decode()
print(b64s)

# emZpxTR+RbbDWMMjGLhDqZjfhWWA2JlXIrHLA3J9KNCmNs2auPTzzi7NhS/ci9cD