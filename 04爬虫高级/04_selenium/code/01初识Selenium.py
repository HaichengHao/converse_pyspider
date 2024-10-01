# @Editor    : 百年
# @FileName  :01初识Selenium.py
# @Time      :2024/9/29 22:38

# selenium 可以自动打开一个浏览器
# 输入网址
# 从页面取出东西
import selenium
import requests
from selenium.webdriver import Chrome

# 先创建一个浏览器对象
# executable_path 指定可执行的chromedriver路径
# options= 指定配置信息,目前还用不到
web = Chrome(executable_path='../others/chromedriver.exe')
url = 'https://www.baidu.com'

# 打开url对应的网址,相当于我们在浏览器的搜索框里输入了百度的网址
web.get(url)

# 接下来从文件里提取出一些东西
print(web.title) #我们拿到网页的标题
# 百度一下，你就知道
