"""
@File    :算法还原.py
@Editor  : 百年
@Date    :2025/6/2 19:51 
"""
#MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB


#逆向过程中最终定位
'''
window.encryptFn = function(e) {
            var o = new JSEncrypt;
            return o.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"),
            o.encrypt(e)
        }
var param = {
        url: '/login/passwordLogin',
        data: {
          userName: username,
          password: encryptFn(pwd + '' + ress.data),
          imageCaptchaCode: imgCode,
        },
      }
        '''

#既然已经把公钥给我们了,而且目测rsa算法,那就对其进行逆向还原
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

pubk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'

#将公钥还原成字节格式
pubk = base64.b64decode(pubk)
pubk = RSA.import_key(pubk)
print(pubk)
#创建解密器
rsa = PKCS1_v1_5.new(key=pubk)
time_s = int(time.time()*1000)   #时间戳
passwd = input('请输入明文密码')   #输入明文密码
data = str(passwd+' '+str(time_s))  #对其进行拼接
print(data)
print(type(data))
sec_message = rsa.encrypt(data.encode())
print(sec_message)
print(base64.b64encode(sec_message))  #输出b64格式

