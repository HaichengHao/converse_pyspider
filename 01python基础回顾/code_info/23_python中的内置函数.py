# editor: 百年
# time: 2024/3/6 17:04
'''
# 数值运算
# bin oct hex 二进制，十进制，十六进制
print(bin(8))
print(oct(8))
print(hex(8))
# 0b1000
# 0o10
# 0x8

# sum min max pow 求和，最小值，最大值，开方

# 求和时，要用[]括起来
print(sum([1,2,3,4,5]))

print(min(1,2))
# 超过两个数求最小值也是用[]括起来
print(min([4,13,2,11,5]))

print(max(1,2))
# 超过两个数求最大值也是用[]括起来
print(max([4,13,2,11,5]))
# 13


print(pow(2,3)) #相当于2**3 即2的三次方
# 8'''

# 字符串操作
# 切片操作slice()
s=slice(1,4,2)
str='哈呵，笑死我了'
print(str[s])
# 呵笑 <--从1切到4，取切出来的两个

# ord()和chr()
first_name='张'
print(ord(first_name))
# 24352
print(chr(24352))
# 张

num=16
print(format(num,'b'))
# 10000   后面指定了b即为转成二进制数
print(format(num,'x'))
# 10  转换成16进制数
print(format(num,'o'))
# 20  转成8进制

# 还可进行补全操作
print(format(num,'08b'))  #<--意思是补全为8位二进制数
# 00010000  <--补全了

# enumerate枚举
lst_1=['张三丰','张无忌','张大炮']
for item in enumerate(lst_1):
    print(type(item))
    print(item)
# (0, '张三丰')
# (1, '张无忌')
# (2, '张大炮')
# all <--把它当成and来看
print(all(['哈哈','今儿','吃饭']))
# True <--都是实字符串，非空，即为真
print(all([0,1,1]))
# False <-- 数字0的布尔值为False
# any <--把它当成or来看

# 哈希计算
s='不过如此'
print(hash(s))
# 8522959841574458248 <--字符串的哈希值
# 注意，列表和字典是不可哈希的，因为它们是可变的
# 利用算法将数据转换为内存地址然后进行数据的存储 <--哈希表

print(dir(print()))
# ['__bool__', '__class__', '__delattr__',
# '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__',
# '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__']