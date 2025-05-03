"""
@File    :07随机字节.py
@Editor  : 百年
@Date    :2025/5/3 10:08 
"""

# tips:低于3.9的是没有这个功能的
import random

data = random.randbytes(10)
print(data)
# b'R\xb1\xed\x9f\x01;\xb5q\xdd;' 得到了字节序列
# 一般对字节一循环得到的都是其对应的十进制的表示
print([i for i in data])

# [82, 177, 237, 159, 1, 59, 181, 113, 221, 59]

# tips:java中一般会将得到的结果.toString(16)，也就是将其转换成16进制形式且转换为字符串
ele_list = []
ele_raw_lst = []  # 写一个列表来拿未处理的带进制标识的数据
for item in data:
    ele = hex(item)
    ele_raw_lst.append(ele)
res1 = "".join(ele_raw_lst)
'''0xb40x4a0x900x450x930x7e0xee0x320x6c0x9a'''
print(res1)
for item in data:  # tips:因为循环拿到的元素都是十进制的，然后要将其转换为16进制
    ele = hex(item)[2:]  # tips:这里为什么要用到字符串分片呢?因为python转换别的进制到16进制会在其前面加上标识0x(除了十进制不会加)，所以我们只要非标识的
    # 二进制会加0b
    ele_list.append(ele)
res = "".join(ele_list)  # tips:列表元素拼接为字符串
print(res)
'''b44a9045937eee326c9a'''

# tips:也可以直接写 res3 = "".join([hex(item)[2:] for item in data])
lst_ = [hex(item)[2:] for item in data]
res2 = "".join(lst_)
print(res2)

# 最短写法,且加上补0操作
res3 = "".join([hex(item)[2:].rjust(2, "0") for item in data])
print(res3)

# tips:或者利用字符串格式化,这样可以直接去掉进制标识前缀
# tips:%02x可以实现不满两位就在前面补充0字符
res4 = "".join(["%02x" % (item,) for item in data])
print(res4)
