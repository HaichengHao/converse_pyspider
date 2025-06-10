"""
@File    :final.py
@Editor  : 百年
@Date    :2025/6/3 19:30 
"""

# 最后的正确修改
# import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def pwdenc(passwd,timedata):
    pubk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'

    #将公钥还原成字节格式
    pubk = base64.b64decode(pubk)
    pubk = RSA.import_key(pubk)
    # print(pubk)
    #创建加密器
    rsa = PKCS1_v1_5.new(key=pubk)

    data = passwd+str(timedata)  #对其进行拼接

    # 加密的是字节,永远记住这一点,所以要encode
    sec_message = rsa.encrypt(data.encode('utf-8'))
    # print(sec_message)
    # print(base64.b64encode(sec_message))  #输出b64格式
    encrypt_pwd = base64.b64encode(sec_message).decode()
    return encrypt_pwd
# if __name__ == '__main__':
#     encrypt_data = pwdenc('HHCzio20.','1748959427647')
#     print(encrypt_data)