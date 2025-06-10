"""
@File    :08非对称加密RSA.py
@Editor  : 百年
@Date    :2025/6/1 10:26 
"""
'''
非对称加密,加密和解密的密钥不是同一个密钥,而是需要两把密钥
一个是公钥,一个是私钥,公钥发送给客户端,发送端用公钥对数据进行加密,
再发送给接收端,接收端使用私钥来对数据进行解密,
由于私钥只存放在接收端这边,
所以即使数据被截获了,也是无法进行解密的
常见的非对称加密算法:RSA,DSA
rsa是最常见的一种加密方案 
公钥是用来加密的
私钥是用来解密的
密钥(私钥)不能公开
公钥和私钥是成对的,是有一定的关联的 
加密和解密用的不是同一个密钥，私钥放在服务器上不公开
'''
from Crypto.PublicKey import RSA  #这是处理密钥的
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import base64
# 生成密钥,默认生成的是私钥
key = RSA.generate(2048)
print(key)
# Private RSA key at 0x1D92A324690  生成了私钥,后面跟的是内存地址

# print(key.export_key())
# print(key.exportKey()) #tips:这俩一样的
private_key = key.export_key()
# print(private_key)
#直接这样输出的是base64字节而且带有换行符
# 可以decode,将base64字节转换为b64字符串
print(private_key.decode())

# private_key_b = key.export_key(format='DER') #输出纯字节的私钥
# print(private_key_b)


#生成公钥

puiblic_key = key.public_key()
print(puiblic_key)
# Public RSA key at 0x227A7D9ADD0
print(puiblic_key.export_key())
#这样打印也是有换行符的
print(puiblic_key.export_key().decode())
#还得decode
'''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTelupiUOptxRuq0HdXe
wvxw7mfpE45uxPGybbFWCykczUjthcsrnfe33zX6GikGN8O/h1Z2LGvslkupeGYB
mixLnTMTahL45P2o92szSb9xiixa50FrfFCwkkuCTcpHARkMDMawAIH+xt+bKjq9
DJKHXTaTpjrcaqXI38TYwMtGYRFJhOQr39B3P28UNAa03gKbajh4sRSA0WF6I8My
wdZZmmccW6q+rgZOs92UCwUTd4ZmzweU2FQeailhLrQWTbO9g/w9HLtFFgUWx6Vf
2WO8S5zEBPFHqbvh1Kjtvn9HK+w12uM7NDBdLgMg0PgU9AfGNzDj2pOU+drdPzbM
uwIDAQAB
-----END PUBLIC KEY-----
'''

#这正使用过程中,服务器一开始就会直接写入到文件当中去


#important:注意写入的是二进制
#写出私钥
with open('private.pem','wb') as f:
    f.write(key.export_key())

#写出公钥
with open('public.pem','wb') as f1:
    f1.write(key.public_key().export_key())

