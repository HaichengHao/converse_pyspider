"""
@File    :02aes加密16进制字节处理.py
@Editor  : 百年
@Date    :2025/4/17 13:33 
"""
# important:可以先回看python基础中的进制转换
v1 = "AE30AFED57A22A35BC160AB10"
print(len(v1))
binary_str = bytearray() #调用btyearrt创建字节数组
for i in range(0,len(v1),2): #每两个字符作为一组来进行编码
    item_hex = v1[i:i+2] #tips:这里就是说拿到字符i到字符i+2(不包含i+2)的两个字符
    #然后将16进制转换为10进制
    item_decimal = int(item_hex,16)
    #再将转化为16进制的数据添加到字节数组当中
    binary_str.append(item_decimal)

v3 = bytes(binary_str) #然后将字节数组转为二进制
print(v3)
# b'\xae0\xaf\xedW\xa2*5\xbc\x16\n\xb1\x00'
