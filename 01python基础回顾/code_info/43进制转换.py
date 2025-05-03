"""
@File    :43进制转换.py
@Editor  : 百年
@Date    :2025/3/30 21:43 
"""

# tips:int(b/o/h,2/8/16) 可以很方便的将2、8、16进制数转为十进制
# important:十进制是“和事佬”它可以实现各个进制之间的转换的纽带作用


# important:二进制转换
binary_num = '10110100'
decimal_num = int(binary_num,2) #二进制转换为十进制
octal_num = oct(decimal_num) #十进制转八进制
hexadecimal_num = hex(decimal_num) #十进制转16进制




# important:八进制转换
octal_num1 = '52'
decimal_num1 = int(octal_num1,8)
binary_num1 = bin(decimal_num1)
hexadecimal_num1 = hex(decimal_num)

# important:十进制转换
decimal_num2 = 30
print('十进制数为',decimal_num2)
print('转换为二进制为',bin(decimal_num2))
print('转换为八进制为',oct(decimal_num2))
print('转为十六进制为',hex(decimal_num2))


# important:十六进制转换
hexadecimal_num2 = '2a'
decimal_num3  = int(hexadecimal_num2,16)
binary_num3  = bin(decimal_num3)
octal_num = oct(decimal_num3)