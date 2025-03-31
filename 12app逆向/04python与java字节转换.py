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

java_byte_list = [19,-50,-29,-22,-71,-90]
python_byte_list = []
#也可以这样声明
# python_byte_list = bytearray()

for item in java_byte_list:
    if item < 0:
        item = item+256
        python_byte_list.append(item)
    else:
        python_byte_list.append(item)

print(python_byte_list)

# str_data = python_byte_list.decode('gbk')
# print(str_data)

