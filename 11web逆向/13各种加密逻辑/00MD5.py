"""
@File    :00MD5.py
@Editor  : 百年
@Date    :2025/5/27 18:24 
"""
'''
md5本身不是一种加密算法，而是摘要算法，其是不可逆的'''

#导入需要的包
from hashlib import md5

#step1:创建一个加密对象
# obj = md5()

# tips:为了防止撞库,MD5创建阶段可以进行加盐
obj = md5(b'weixiaozaimeizaitianbushinidedoubutebie')

#step2:给加密对象增加内容,字符串必须在哈希前进行编码
# 其实说白了就是加密的必须是字节
obj.update("hello , aloha".encode('utf-8'))

obj.update('yes,i am ironman'.encode('utf-8'))

#step3:看结果,往往会导出32位的16进制数字
result = obj.hexdigest()

print(result)
# ce83402ae45ff730cefa39de5f7279d5

# important:python计算的md5是标准的md5算法，但是网页端可能会遇到魔改的md5!!!
#  如果是标准的可以用python来完成,魔改的话就扣代码