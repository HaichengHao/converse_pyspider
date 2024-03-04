# editor: 百年
# time: 2024/3/3 21:27
print(2**64)


# 2
s="乔布斯"

# 对文字进行编码，标准为utf-8
bs_utf=s.encode('utf-8')
bs_gbk=s.encode('gbk')
print(bs_utf,'\n',bs_gbk)
# b'\xe4\xb9\x94\xe5\xb8\x83\xe6\x96\xaf'
#  b'\xc7\xc7\xb2\xbc\xcb\xb9'

# b'xxxx' 为bytes类型数据 一个'\x'划分一个字节
# 可见utf-8一个汉字三个字节，gbk则是两个字节

# 怎么把gbk与utf-8相互转换？
# 其实就是先把要转化的字符二进制编码转换成字符串，再以目标形式转换出来即可

s_utf=bs_utf.decode('utf')
print(s_utf)
# 乔布斯

# 变成正常文字之后再进行编码
s_gbk=s_utf.encode('gbk')
print(s_gbk)
# b'\xc7\xc7\xb2\xbc\xcb\xb9' <--转换成功

s_1='你好世界abc'
s_1utf=s_utf.encode("utf-8")
print(s_1utf)
# b'\xe4\xb9\x94\xe5\xb8\x83\xe6\x96\xaf'
