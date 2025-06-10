"""
@File    :04base64.py
@Editor  : 百年
@Date    :2025/5/30 10:44 
"""
'''
加密或者解密的时候结果通通都是字节,密文是用来传输的,但是在http协议里传输字节
是一件很麻烦的工作,相对应的，如果传输的是字符串就好控制的多,此时base64应运而生
26个大写字母+26个小写字母+10个数字+2个特殊符号(+和/)组成了一组类似与64进制的计算逻辑
这就是base64'''
import base64
bs = "天空好像下雨".encode('utf-8')
print(bs)  #首先整一个字符串转换成字节
# b'\xe5\xa4\xa9\xe7\xa9\xba\xe5\xa5\xbd\xe5\x83\x8f\xe4\xb8\x8b\xe9\x9b\xa8'
# important:把字节转换成base64编码的字节
print(base64.b64encode(bs))
# b'5aSp56m65aW95YOP5LiL6Zuo' 注意还是b打头,说明还是字节
print(base64.b64encode(bs).decode())  #tips:对b64的字节进行解码
# 5aSp56m65aW95YOP5LiL6Zuo

"""
总结:杂乱的字节转换成base64字符串 
base64.b64encode(bytes).decode()
将base64字符串还原成正常的字符串
base64.b64decode(b64str).encode()
"""


#tips:将字符串进行b64编码成b64的字节然后再进行转码
b64s = base64.b64encode(bs).decode()
# 把b64字符串解码为b64的字节
print('要进行转换的数据',b64s)
# 要进行转换的数据 5aSp56m65aW95YOP5LiL6Zuo
print(base64.b64decode(b64s))
# b'\xe5\xa4\xa9\xe7\xa9\xba\xe5\xa5\xbd\xe5\x83\x8f\xe4\xb8\x8b\xe9\x9b\xa8'
print(len(base64.b64encode(bs)))
# 24 important:注意base64编码的字节长度一定是4的倍数
#important:将b64的字节解码并'可以指定'解码的编码规则是utf-8
print(base64.b64decode(b64s).decode())  #important:b64decode
print(base64.b64decode(b64s).decode('utf-8'))
# 天空好像下雨
# 天空好像下雨