"""
@File    :13selenium操作已经打开的浏览器.py
@Editor  : 百年
@Date    :2025/4/21 12:50 
"""
import time

'''
chrome://version 先在chrome里查看自己的chrome可执行路径
然后转到这个路径
执行下面的命令
chrome --remote-debugging-port=9527 这样就会直接打开本机的浏览器
chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium" 如果这样写的话就会开一个新的浏览器

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 接管已经打开的浏览器
options = Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9528")
browser = webdriver.Chrome(options=options)
browser.get('https://www.bilibili.com/')
time.sleep(6)
print(browser.title)