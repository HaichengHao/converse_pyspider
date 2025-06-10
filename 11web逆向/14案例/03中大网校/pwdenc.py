"""
@File    :pwdenc.py
@Editor  : 百年
@Date    :2025/6/3 18:22 
"""
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
def pwdenc(passwd):
    pubk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'

    #将公钥还原成字节格式
    pubk = base64.b64decode(pubk)
    pubk = RSA.import_key(pubk)
    # print(pubk)
    #创建加密器
    rsa = PKCS1_v1_5.new(key=pubk)
    time_s = int(time.time()*1000)   #时间戳
    # passwd = input('请输入明文密码')   #输入明文密码
    data = str(passwd+' '+str(time_s))  #对其进行拼接
    # print(data)
    # print(type(data))
    sec_message = rsa.encrypt(data.encode())
    print(sec_message)
    print(base64.b64encode(sec_message))  #输出b64格式
    encrypt_pwd = base64.b64encode(sec_message).decode()
    return encrypt_pwd
# if __name__ == '__main__':
#     encpwd = pwdenc('123456')
#     print(encpwd)


# 后来发现其实这样写是有问题的,因为时间戳非常恶毒,不是当前的时间戳,而是有一个ajax请求
# 那个请求的响应里头是这样的
'''
{
    "code": 0,
    "msg": null,
    "data": "1748947848333",
    "operation_date": "2025-06-03 18:50:48"
}'''

#important:要获得的就是data,所以此次改写本质上是有疏漏的