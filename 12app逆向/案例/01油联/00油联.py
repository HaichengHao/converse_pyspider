"""
@File    :00油联.py
@Editor  : 百年
@Date    :2025/4/12 19:37 
"""
import time

'''
POST /app/api/v1/partnerLogin/login HTTP/1.1
X-App: native
X-Noncestr: 123456
X-OS: partnerApp_android
X-Req-Time: 1744456481437   时间戳
X-Sign: 8a3b8440570dc58c5b90d2c330494a1f  这个也需要注意
X-Token: 
X-UserID: 
Content-Type: application/x-www-form-urlencoded
Content-Length: 59
Host: chinayltx.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.10.0

phone=16868941234&password=e10adc3949ba59abbe56e057f20f883e   可以看到密码被加密了


新:
POST /app/api/v1/partnerLogin/login HTTP/1.1
X-App: native
X-Noncestr: 123456
X-OS: partnerApp_android
X-Req-Time: 1744631655959
X-Sign: 5523c2c12f917d0a07d7fb524ab4c51e
X-Token: 
X-UserID: 
Content-Type: application/x-www-form-urlencoded
Content-Length: 59
Host: chinayltx.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.10.0

phone=19897064163&password=e10adc3949ba59abbe56e057f20f883e
需要解决的主要问题，xsign和passwd,需要利用jadx反编译apk文件
经过jadx反编译apk文件发现用的是md5加密,所以利用00md5加密可以看到123456明文加密后确实与密文一致了
phone=19897064163&password=e10adc3949ba59abbe56e057f20f883e
X-Sign: 5523c2c12f917d0a07d7fb524ab4c51e
反编译出的X-sign
private String sign(String str) {
        return Md5.md5(this.token + this.reqTime + this.noncestr.substring(2) + str).toLowerCase();
    }
this.token =""
this.reqTime = 时间戳
this.noncestr.substring(2)相当于this.noncestr[2:] 即从索引位置为2到最后,即3456
str = "phone=19897064163&password=e10adc3949ba59abbe56e057f20f883e"
所以全部的就是他们拼接起来就行了然后再进行md5加密
'''
import requests
import hashlib

token =""
# reqTime = int(time.time()*1000)
reqTime = '1744631655959'
noncestr = '123456'
substr_ = noncestr[2:]
str = "phone=19897064163&password=e10adc3949ba59abbe56e057f20f883e"
encrypt_str = f'{token}{reqTime}{substr_}{str}'

obj = hashlib.md5()
obj.update(encrypt_str.encode('utf-8'))
res = obj.hexdigest()
print(res)
'''runtime_result
5523c2c12f917d0a07d7fb524ab4c51e  对比一下,x-sign确实已经正确获得了'''
# headers={
#     'User-Agent': 'okhttp/3.10.0'
# }
# data={
#
# }
# url = 'https://chinayltx.com/app/api/v1/partnerLogin/login'
# response = requests.post(url=url,heaers=headers,data=data)