"""
@File    :13selenium操作已经打开的浏览器.py
@Editor  : 百年
@Date    :2025/4/21 12:50 
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 接管已经打开的浏览器
options = Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
browsesr = webdriver.Chrome(options=options)
browsesr.get('https://www.bilibili.com/')
print(browsesr.title)