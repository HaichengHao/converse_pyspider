"""
@File    :09使用自己的rsa密钥加密.py
@Editor  : 百年
@Date    :2025/6/2 10:00 
"""

'''
加密流程是客户端最有用的地方
解密流程是发生在服务器端的
'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

#step1 :加载密钥,需要的是公钥,公钥是用来加密的
#这里用我们上一个文件中生成的公钥
#export是导出,那么我们就可以用import进行导入
# tips: 可以读字节import_key(b'b64密钥',),也可以读字符串
pub_k = RSA.import_key(open('public.pem','rb').read())
#step2 :创建加密器的流程和之前的AES,DES很像
rsa = PKCS1_v1_5.new(key=pub_k)

#step3 :进入加密逻辑
s = 'hello,我叫hero,你是??'
enc_s = rsa.encrypt(s.encode('utf-8'))

print(enc_s)
#打印出来是混乱字节
#step4 :为了传输,需要利用base64进行编码

enc_s = base64.b64encode(enc_s)
print(enc_s.decode())
#important:rsa加密后的东西,如果不是纯数学算法,每次都是随机的

