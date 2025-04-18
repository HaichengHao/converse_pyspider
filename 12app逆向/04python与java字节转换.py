"""
@File    :04python与java字节转换.py
@Editor  : 百年
@Date    :2025/3/31 16:43 
"""
'''
//[-80, -39, -60, -22]
//[-25, -103, -66, -27, -71, -76]
//java中的字节都是有符号的，从-128-127  0 1 2 3 4 .....127 -128 -127 -126 ... -2 -1
//python中的字节都是无符号的,从0-255    0 1 2 3 4..... 127  128  129  130 ... 254 255
//两者之间如何转换呢？ 如对应-128 对应 128 -127对应 129  -- pythonb = javab + 256
'''

# java_byte_list = [19,-50,-29,-22,-71,-90]
# python_byte_list = []
# #也可以这样声明
# # python_byte_list = bytearray()
#
# for item in java_byte_list:
#     if item < 0:
#         item = item+256
#         python_byte_list.append(item)
#     else:
#         python_byte_list.append(item)
#
# print(python_byte_list)
#
# # str_data = python_byte_list.decode('gbk')
# # print(str_data)


# 还有一种方法，那就是使用ctypes,让python输出的整形表现为类似于c语言和java亦或是javascript的有符号整型
import ctypes
v1 = 111222333444;
v2 = 111222333444 << 5; #相当于v1 * 10^5
result = ctypes.c_int32(v2).value  #important:相当于调用ctype中c语言的整形(int 4字节)表示v2且返回表示的值value
#                                       并用result接收
print(result)
# -1413218176 成功
