"""
@File    :01油联.py
@Editor  : 百年
@Date    :2025/4/12 19:37 
"""
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


需要解决的主要问题，xsign和passwd,需要利用jadx反编译apk文件
经过jadx反编译apk文件发现用的是md5加密,所以利用00md5加密可以看到123456明文加密后确实与密文一致了
'''
import requests
headers={
    'User-Agent': 'okhttp/3.10.0'
}
data={

}
url = 'https://chinayltx.com/app/api/v1/partnerLogin/login'
response = requests.post(url=url,heaers=headers,data=data)