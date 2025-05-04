"""
@File    :13Base64编码.py
@Editor  : 百年
@Date    :2025/5/4 12:29 
"""
import base64
name = 'nikofox'
res = base64.b64encode(name.encode('utf-8'))
print(res)


data = base64.b64decode(res)
print(data)
origin = data.decode('utf-8')
print(origin)

# b'bmlrb2ZveA=='
# b'nikofox'
# nikofox