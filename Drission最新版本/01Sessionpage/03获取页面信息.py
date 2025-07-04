"""
@File    :03获取页面信息.py
@Editor  : 百年
@Date    :2025/7/3 19:38 
"""
from DrissionPage import SessionPage
# 成功访问网页后，可使用`SessionPage`自身属性和方法获取页面信息。

page = SessionPage()
page.get('https://www.baidu.com')

print(page.title)
print(page.html)
print(page.url)

print(page.url_available) #此属性以布尔值返回当前链接是否可用。

print(page.raw_data) #此属性返回访问到的元素数据，即`Response`对象的`content`属性。返回的是二进制对象

print(page.json)
# 此属性把返回内容解析成 json。
# 比如请求接口时，若返回内容是 json 格式，用`html`属性获取的话会得到一个字符串，用此属性获取可将其解析成`dict`。
# 支持访问 `*.json` 文件，也支持 API 返回的json字符串。
# **类型：**`dict`

print(page.user_agent)

# 运行参数信息
page2 = SessionPage(timeout=5)
# 修改 timeout
page2.timeout = 20


# retry_times 此属性为网络连接失败时的重试次数。默认为 3，可对其赋值。
# 修改重复次数
page2.retry_times = 5

# retry_interval
# 此属性为网络连接失败时的重试等待间隔秒数。默认为 2，可对其赋值。
# # 修改重试等待间隔时间

page2.retry_interval = 1.5

#encoding
#
# 此属性返回用户主动设置的编码格式。
page2.encoding = 'utf-8'



