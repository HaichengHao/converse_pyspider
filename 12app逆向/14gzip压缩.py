"""
@File    :14gzip压缩.py
@Editor  : 百年
@Date    :2025/5/4 12:50 
"""
import gzip

# 压缩
s_in = "you love u".encode('utf-8')
s_out = gzip.compress(s_in)

print([i for i in s_out])
# [31, 139, 8, 0, 104, 242, 22, 104, 2, 255, 171, 204, 47, 85, 200, 201, 47, 75, 85, 40, 5, 0, 30, 86, 246, 144, 10, 0, 0, 0]

# 解压缩
res = gzip.decompress(s_out)
print(res)
# b'you love u'

print(res.decode('utf-8'))
# you love u
