"""
@File    :02结束.py
@Editor  : 百年
@Date    :2025/4/14 20:36 
"""

'''从错误信息来看，问题出在 SSL 证书验证失败。具体来说，requests 库在尝试通过 HTTPS 连接到 chinayltx.com 时，发现该网站使用了自
签名证书（self-signed certificate），而不是由受信任的证书颁发机构（CA）签发的有效证书。'''
import hashlib
import time
import urllib3

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

url = 'https://chinayltx.com/app/api/v1/partnerLogin/login'

phonenumber = input('输入手机号>>')
passwd = input('输入密码>>')
obj0 = hashlib.md5(passwd.encode('utf-8'))
sign_pwd = obj0.hexdigest()
token = ""
reqTime = str(int(time.time() * 1000))
noncestr = '123456'
substr_ = noncestr[2:]
str = f"phone={phonenumber}&password={sign_pwd}"
encrypt_str = f'{token}{reqTime}{substr_}{str}'
obj1 = hashlib.md5()
obj1.update(encrypt_str.encode('utf-8'))
x_sign = obj1.hexdigest()
headers = {
    'X-App': 'native',
    'X-Noncestr': '123456',
    'X-OS': 'partnerApp_android',
    'X-Req-Time': reqTime,
    'X-Sign': x_sign,
    'X-Token': '',
    'X-UserID': '',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '59',
    'Host': 'chinayltx.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.10.0',
}
data = {
    'phone': phonenumber,
    'password': sign_pwd
}
response = requests.post(url=url, headers=headers, data=data, verify=False)
response.encoding = response.apparent_encoding
page_source = response.text
print(page_source)


# D:\venvs\converse_pyspider\Scripts\python.exe E:/converse_spider/converse_pyspider/12app逆向/案例/01油联/02结束.py
# 输入手机号>>19897064163
# 输入密码>>123456
# D:\venvs\converse_pyspider\Lib\site-packages\urllib3\connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request is being made to host 'chinayltx.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
#   warnings.warn(
# {"msg":"用户没有注册"}成功!!

