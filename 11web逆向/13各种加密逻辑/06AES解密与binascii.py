"""
@File    :06AES解密.py
@Editor  : 百年
@Date    :2025/5/31 9:49 
"""
#因为是对称加密所以密钥模式以及iv都得是一样的
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad #有补长度就有反操作


raw = 'IEGEnUcCtbHtybVqdIVUfdmBey50R/RBZ/pt2ly4MAE='

#将数据还原成之前的字符串格式
aes = AES.new(key=b'0123456789abcdef',mode=AES.MODE_CBC,iv=b'0123456789123456')

#注意如果想还原那么就得将其转换为字节
import base64
b64s = base64.b64decode(raw)
print(b64s)

#解密之后unpad

decs = aes.decrypt(b64s)

res = unpad(decs,16)
print(res.decode('utf-8'))
# 你好,世界,hello world
'''
解密和加密的步骤刚好是反着来的'''



#important:
'''
有时候有的网页会把IV写成16进制的数字以0x开头  
例如0xadifeabb1aifuoaea2
这时候就需要
俩都试一下,哪个不报错哪个就是成功的
import binascii
a2b_hex()可以将16进制数字转换为字节
binascii.a2b_hex(去掉0x的剩余段adifeabb1aifuoaea2)
b2a_hex()可以将字节转换为16进制数字
binascii.b2a_hex()
其实区分iv到底是16进制还是base64字符串有很好的办法
就是看组成,因为0x的字母是a-f,所以绝对不可能有大于f的出现

'''


