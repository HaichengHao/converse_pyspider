"""
@File    :02更方便的处理方式.py
@Editor  : 百年
@Date    :2025/4/17 13:59 
"""
'''
转换成16进制和这种方便处理的方式和01的不同之处就在于对于key和iv这种会对字节做特殊的处理，所以结果不同'''
import binascii
v1 = "AE30AFED57A22A35BC160AB1A0" #明文
# 将16进制解码为字节a to b
v3 = binascii.a2b_hex(v1)
# 注意有a2b也有b2a
print(v3)

# b'\xae0\xaf\xedW\xa2*5\xbc\x16\n\xb1\xa0'

# 有了a2b也有b2a,下面将密文还原成明文
v4 = binascii.b2a_hex(v3).decode().upper()
print(v4)
# AE30AFED57A22A35BC160AB1A0 还原成明文成功

'''
在逆向过程之中要先使用没有key/iv/salt的这种处理方式，如果得出的结果和目标不同再考虑逆向iv/key/salt来进行处理'''