"""
@File    :main.py
@Editor  : 百年
@Date    :2025/6/2 21:14 
"""

# 可以发现后续获取图片时候的参数传入有sessionid,这个id是登录页面请求生成的
import base64
import json

import requests
from final import pwdenc
from chaojiying import Chaojiying_Client

# from pwdenc import encpwd
session = requests.session()
session.headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}
login_url = 'https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2Fexampoint%2Flist%3Fsign%3Djz1'

response = session.get(url=login_url)
# print(response.cookies)
# <RequestsCookieJar[<Cookie sessionId=1748871354729 for user.wangxiao.cn/>]>  这样就得到了sessionid


# 加载验证码链接
img_resp = session.post(
    url='https://user.wangxiao.cn/apis//common/getImageCaptcha',
    headers={
        'content-type': 'application/json; charset=utf-8'
    }
)

#   # 打印请求头
'''
{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 
'Connection': 'keep-alive', 'content-type': 'application/json; charset=utf-8', 'Cookie': 'sessionId=1748872390575', 
'Content-Length': '0'}
'''
# print(img_resp.headers)  # 响应头
'''
{'Server': 'nginx/1.24.0', 'Date': 'Mon, 02 Jun 2025 13:53:10 GMT', 'Content-Type': 'application/json; charset=utf-8',
 'Content-Length': '13176', 'Connection': 'keep-alive', 'X-Frame-Options': 'ALLOWALL'}

'''
# print(img_resp.json()) #打印响应信息
img_json = img_resp.json()
# 要获取data里的内容
data_raw = img_json['data']
# print(data_raw)
# print(data.split(',')[1])
data = img_json['data'].split(',')[1]
# 然后就得到了b64编码的字符串

# 然后需要decode将base64字符串转换为字节,然后进行写入操作
data_b = base64.b64decode(data)
with open('demo.png', 'wb') as f:
    f.write(data_b)

# 利用超级鹰搞定验证码
chaojiying = Chaojiying_Client('minkofox', 'HHCzio20.', '963713')  # 用户中心>>软件ID 生成一个替换 96001
im = open('demo.png', 'rb').read()

result = chaojiying.PostPic(im, 1902)
picstr = result['pic_str']

print(picstr)

# 先要访问那个gettime来获取我们想要的

gettime = session.post(
    url='https://user.wangxiao.cn/apis//common/getTime',
    headers={
        'content-type': 'application/json; charset=utf-8'
    }
)
data_all = gettime.json()

data = gettime.json()['data']

print(data)



# 三者兼备,账号密码和验证码都有了
user_name = '18864771568'
passwd = 'HHCzio20.'
pwd = pwdenc(passwd,data)
#
data2 = {
    'userName': user_name,
    'password': pwd,
    'imageCaptchaCode': picstr

}
#
final_resp = session.post(
    url='https://user.wangxiao.cn/apis//login/passwordLogin',
    headers={
        'content-type': 'application/json; charset=utf-8'
    },
    data=json.dumps(data2)  # 注意,传入的是一个json格式的,所以要用序列化

)
# print(final_resp.headers)
print(final_resp.text)

#
# # 登录成功之后仍然需要按照浏览器的逻辑将cookie补齐
# print(session.cookies)
#
login_info = final_resp.json()['data']
# # 补全cookie
session.cookies['autoLogin'] = 'true'
session.cookies['userInfo'] = json.dumps(login_info)
session.cookies['token'] = login_info['token']
#
session.cookies['UserCookieName'] = login_info['userName']
session.cookies['OldUsername2'] = login_info['userNameCookies']
session.cookies['OldUsername'] = login_info['userNameCookies']
session.cookies['OldPassword'] = login_info['passwordCookies']
session.cookies['UserCookieName_'] = login_info['userName']
session.cookies['OldUsername2_'] = login_info['userNameCookies']
session.cookies['OldUsername_'] = login_info['userNameCookies']
session.cookies['OldPassword_'] = login_info['passwordCookies']
session.cookies[login_info['userName'] + "_exam"] = login_info['sign']

# # 验证是否可用
data3={
    'examPointType': "",
    'practiceType': "2",
    'questionType': "",
    'sign': "cjtxgcs",
    'subsign': "b6893c1dc8899fcc6a7f",
    'top': "30"
}
quiz_list = session.post(
    url='https://ks.wangxiao.cn/practice/listQuestions',
    headers={
        'content-type': 'application/json;charset=UTF-8'
    },
    data=json.dumps(data3)
)
print(quiz_list.json())