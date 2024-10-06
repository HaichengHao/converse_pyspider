# @Editor    : 百年
# @FileName  :01超级鹰使用回顾.py
# @Time      :2024/10/6 19:43
# editor: 百年
# time: 2024/2/17 17:04
import requests
from bs4 import BeautifulSoup
import random
from chaojiying import Chaojiying_Client


# import urllib.request
# 通过登录进入到主界面，验证码也需要破解
'''
通过找登录接口，发现参数有很多
'''
'''
__VIEWSTATE: 1P+nnLhDUUm518TukX/far1KMIPJIALkfqR92M2XrgxgNBkki9wXQr5BnZpnC1vtNeepr2LCbGjR+GkZmqKuHR7bWTrSV+jsDpsKnFjNfhBQVX8/eBih6TblqzequY75lfVcdY1iXCdxFEInmks5PTtpUP0=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: 2020104216@qq.com
pwd: nikofox
code: ALZM
denglu: 登录

# 我们观察到 __VIEWSTATE  __VIEWSTATEGENERATOR  code 是变量

# 难点 验证码 未知请求头参数
一般看不到的数据都在网页源码之中

'''
# 代理池配置
proxies_pool=[
    {'http': '114.106.135.1:8089'},
    {'http': '117.71.133.51:8089'},
    {'http': '36.6.144.251:8089'},
    {'http': '117.69.237.99:8089'},
    {'http': '183.164.243.181:8089'},
    {'http': '117.69.237.83:8089'},
    {'http': '60.174.0.184:8089'},
    {'http': '123.182.58.55:8089'},
    {'http': '117.57.93.253:8089'},
    {'http': '125.87.95.190:8089'},
    {'http': '223.215.177.140:8089'},
    {'http': '183.164.242.216:8089'},
    {'http': '117.57.93.64:8089'},
    {'http': '180.121.131.59:8089'},
    {'http': '117.69.237.239:8089'},
    {'http': '117.71.149.249:8089'},
    {'http': '36.6.145.207:8089'},
    {'http': '114.231.42.49:8089'},
    {'http': '36.6.145.48:8089'},
    {'http': '123.182.58.57:8089'},
    {'http': '183.164.243.153:8089'},
    {'http': '113.121.47.154:9999'},
    {'http': '36.6.145.172:8089'},
    {'http': '183.164.242.203:8089'},
    {'http': '183.164.243.13:8089'},
    {'http': '183.164.242.92:8089'},
    {'http': '36.6.144.195:8089'},
    {'http': '117.69.232.98:8089'},
    {'http': '36.6.144.223:8089'},
    {'http': '113.223.214.223:8089'},
    {'http': '223.215.176.212:8089'},
    {'http': '111.224.11.52:8089'},
    {'http': '117.69.236.104:8089'},
    {'http': '117.71.149.101:8089'},
    {'http': '183.164.243.2:8089'},
    {'http': '36.6.144.53:8089'},
    {'http': '114.106.147.110:8089'},
    {'http': '120.78.194.53:8888'},
    {'http': '117.71.155.178:8089'},
    {'http': '36.6.144.216:8089'},
]
proxies=random.choice(proxies_pool)
print('所用代理为:',proxies)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
}
# 登录页面的网址
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
response=requests.get(url=url,headers=headers,proxies=proxies)
response.encoding='utf-8'
# 获取页面源码
source_code=response.text
# print(source_code)

# 解析页面源码，获取__VIEWSTATEGENERATOR __VIEWSTATE 的值
soup=BeautifulSoup(source_code,'lxml')

# 获取__VIEWSTATE
VIEWSTATE=soup.select('#__VIEWSTATE')[0].attrs.get('value')


# 获取__VIEWSTATEGENERATOR
# todo:如果这里不理解回顾一下bs4
VIEWSTATEGENERATOR=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value') #这里是通过.attrs获取到标签中的属性,其返回的是一个字典,然后再使用字典取值法获取到我们要的value
# print(VIEWSTATE,VIEWSTATEGENERATOR)

# 获取验证码图片
'''
code_url='https://so.gushiwen.cn/RandCode.ashx'
urllib.request.urlretrieve(url=code_url,filename='./au_pic.jpg')
# 获取下载的图片之后，下载到本地，然后观察验证码，观察之后，在控制台输入，将值给code

# 注意，这里有坑，运行之后虽然以为验证码正确，其实是错误的，会提示验证码错误，需要思考原因
code_info=input('请输入验证码:')
# 原因: 单独获取的验证码和登录请求的验证码不是同一个验证码
'''

# 如何解决？ -- 用requests的session()方法，通过session的返回值可以将其变成一个对象
# code_url='https://so.gushiwen.cn/RandCode.ashx'
code = soup.select('#imgCode')[0].attrs.get('src')
print(code)
code_url = 'https://so.gushiwen.cn' + code

session=requests.session()
# 验证码的url的内容
response_code=session.get(code_url)
content_code=response_code.content  #注意，这里要用的是二进制数据，因为下载的是图片
with open('./au_pic.jpg','wb') as bfp:
    bfp.write(content_code)
# code_info=input('请输入验证码:')
chaojiying=Chaojiying_Client('minkofox','HHCzio20.','1004')
im=open('./au_pic.jpg','rb').read()
result=chaojiying.PostPic(im,1004)
# print(result)
# code_info=input('输入验证码')
# 点击登录
url_login_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data={
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        'from: http': '//so.gushiwen.cn/user/collect.aspx',
        'email': ' 2020104216@qq.com',
        'pwd': 'HHCzio20.',
        'code': result,
        'denglu': '登录',
}
# post_proxy=random.choice(proxies_pool)
# 注意，这里也改成了session，这样两个请求会变成‘一个’请求，自然得到的验证码也是正确的验证码
response_post=session.post(url=url_login_post,headers=headers,data=data)
post_content=response_post.text
with open('./poem.html','w',encoding='utf-8') as wfp:
    wfp.write(post_content)
# 通过登陆  然后进入到主页面

'''
通过找登陆接口我们发现 登陆的时候需要的参数很多
_VIEWSTATE: /m1O5dxmOo7f1qlmvtnyNyhhaUrWNVTs3TMKIsm1lvpIgs0WWWUCQHl5iMrvLlwnsqLUN6Wh1aNpitc4WnOt0So3k6UYdFyqCPI6jWSvC8yBA1Q39I7uuR4NjGo=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: 595165358@qq.com
pwd: action
code: PId7
denglu: 登录

我们观察到_VIEWSTATE   __VIEWSTATEGENERATOR  code是一个可以变化的量

难点:(1)_VIEWSTATE   __VIEWSTATEGENERATOR  一般情况看不到的数据 都是在页面的源码中
    我们观察到这两个数据在页面的源码中 所以我们需要获取页面的源码 然后进行解析就可以获取了
    (2)验证码
'''
# import requests
#
# import random
# # 这是登陆页面的url地址
# url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
#
# # 获取页面的源码
# response = requests.get(url = url,headers = headers)
# content = response.text
#
# # 解析页面源码  然后获取_VIEWSTATE   __VIEWSTATEGENERATOR
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(content,'lxml')
#
# # 获取_VIEWSTATE
# viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
#
# # 获取__VIEWSTATEGENERATOR
# viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
#
#
# # 获取验证码图片
# code = soup.select('#imgCode')[0].attrs.get('src')
# code_url = 'https://so.gushiwen.cn' + code
#
# # 有坑
# # import urllib.request
# # urllib.request.urlretrieve(url=code_url,filename='code.jpg')
# # requests里面有一个方法 session（）  通过session的返回值 就能使用请求变成一个对象
#
# session = requests.session()
# # 验证码的url的内容
# response_code = session.get(code_url)
# # 注意此时要使用二进制数据  因为我们要使用的是图片的下载
# content_code = response_code.content
# # wb的模式就是将二进制数据写入到文件
# with open('./au_pic.jpg','wb')as fp:
#     fp.write(content_code)
#
#
#
#
# # 获取了验证码的图片之后 下载到本地 然后观察验证码  观察之后 然后在控制台输入这个验证码 就可以将这个值给
# # code的参数 就可以登陆
#
# code_name = input('请输入你的验证码')
#
#
# # 点击登陆
# url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
# proxies_pool=[
#     {'http': '36.6.144.113:8089'},
#     {'http': '114.231.8.216:8888'},
#     {'http': '114.231.41.219:8089'},
#     {'http': '182.34.35.230:9999'},
#     {'http': '117.57.93.165:8089'},
#     {'http': '117.69.236.101:8089'},
#     {'http': '111.224.10.250:8089'},
#     {'http': '121.230.211.179:8089'},
#     {'http': '183.164.242.91:8089'},
#     {'http': '113.121.39.222:9999'},
#     {'http': '117.69.159.208:41122'},
#     {'http': '117.69.236.166:8089'},
#     {'http': '114.231.42.96:8089'},
#     {'http': '117.57.93.109:8089'},
#     {'http': '117.57.92.179:8089'},
#     {'http': '117.57.92.89:8089'},
#     {'http': '183.164.243.89:8089'},
#     {'http': '114.106.172.198:8089'},
#     {'http': '114.231.42.80:8888'},
#     {'http': '144.255.49.110:9999'},
#     {'http': '182.34.33.232:9999'},
#     {'http': '117.71.155.254:8089'},
#     {'http': '117.69.237.213:8089'},
#     {'http': '113.223.215.34:8089'},
#     {'http': '117.71.132.21:8089'},
#     {'http': '117.69.237.81:8089'},
#     {'http': '114.231.82.132:8089'},
#     {'http': '114.232.110.230:8089'},
#     {'http': '36.6.144.78:8089'},
#     {'http': '183.164.243.104:8089'},
#     {'http': '117.57.93.72:8089'},
#     {'http': '117.69.233.40:8089'},
#     {'http': '113.223.212.89:8089'},
#     {'http': '117.71.149.176:8089'},
#     {'http': '113.223.213.243:8089'},
#     {'http': '183.164.243.71:8089'},
#     {'http': '117.69.237.202:8089'},
#     {'http': '114.232.110.39:8888'},
#     {'http': '117.69.237.173:8089'},
#     {'http': '114.232.109.73:8089'},
# ]
# proxies=random.choice(proxies_pool)
# data_post = {
#     '__VIEWSTATE': viewstate,
#     '__VIEWSTATEGENERATOR': viewstategenerator,
#     'from': 'http://so.gushiwen.cn/user/collect.aspx',
#     'email': '2020104216@qq.com',
#     'pwd': 'HHCzio20.',
#     'code': code_name,
#     'denglu': '登录',
# }
#
# response_post = session.post(url = url, headers = headers, data = data_post,proxies=proxies)
#
# content_post = response_post.text
#
# with open('./poem.html','w',encoding= ' utf-8')as fp:
#     fp.write(content_post)


# 难点
# （1） 隐藏域
# （2） 验证码
