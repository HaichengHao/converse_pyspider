"""
@File    :07DES解密.py
@Editor  : 百年
@Date    :2025/5/31 15:46 
"""
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64
#b64字符串
b64s = 'emZpxTR+RbbDWMMjGLhDqZjfhWWA2JlXIrHLA3J9KNCmNs2auPTzzi7NhS/ci9cD'

#创建加密对象
des = DES.new(key=b'abcdefjs',mode=DES.MODE_CBC,iv=b'0s23q5q7')

#处理b64字符串,将其还原成字节
b64bs = base64.b64decode(b64s)
print(b64bs)
# b'zfi\xc54~E\xb6\xc3X\xc3#\x18\xb8C\xa9\x98\xdf\x85e\x80\xd8\x99W"\xb1\xcb\x03r}(\xd0\xa66\xcd\x9a\xb8\xf4\xf3\xce.\xcd\x85/\xdc\x8b\xd7\x03'


#进行解密
#注意,还要去掉多余的补齐位置的字符,所以利用unpad
descs = des.decrypt(b64bs)
print(descs)
# b'\xe5\xa4\xa9\xe7\xa9\xba\xe5\xa5\xbd\xe5\x83\x8f\xe4\xb8\x8b\xe9\x9b\xa8,the sky seem to be raining\x03\x03\x03'
s = unpad(descs,8)
print(s.decode('utf-8'))
# 天空好像下雨,the sky seem to be raining