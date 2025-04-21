"""
@File    :17小整合.py
@Editor  : 百年
@Date    :2025/4/21 18:20 
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
os.system(r'start chrome --remtoe-debugging-port=9527')

input("输入空格开始>>")
options = Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
browser = webdriver.Chrome(options=options)
browser.get('https://www.bilibili.com/')
print(browser.title)
time.sleep(2)
page_source = browser.page_source
print(page_source)
