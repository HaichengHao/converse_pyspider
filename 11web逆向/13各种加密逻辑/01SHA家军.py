"""
@File    :01SHA家军.py
@Editor  : 百年
@Date    :2025/5/27 19:54 
"""
'''
sha1
sha256
sha512均为sha系列的
随着数字的增大复杂度也增加
sha系列也是hash散列摘要算法,写法几乎是和md5一致'''

from hashlib import sha1

#step1 创建加密对象
obj = sha1(b'liangnianbankunkun') #tips：加盐

#step2 传入要加密的数据
obj.update('derder'.encode('utf-8'))

#step3 输出结果
res = obj.hexdigest()

print(res)

# e6aaa600018a9e1b198b7529ce34d3f5f7cd184b