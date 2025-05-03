"""
@File    :14操纵打开的浏览器popen.py
@Editor  : 百年
@Date    :2025/4/21 17:59 
"""
'''之前的还需要在cmd里执行,下面写的直接调用python来执行
os.popen
'''

# 第一种有两种写法
# tips:第一种写法(推荐)
import os
os.popen(r'start chrome.exe --remtoe-debugging-port=9527') #important:注意这里写了start
# os.popen(r'start chrome.exe --remote-debugging-port=9527 --user-data-dir="F:\selenium\"') 或者这样打开新的环境

# tips:第二种写法，先转到自己的可执行路径(在chrome里输入chrome://version)查看
# os.chdir(r'C:\Program Files\Google\Chrome\Application')
# os.popen(r'chrome.exe --remtoe-debugging-port=9527')
# os.popen(r'chrome.exe --remote-debugging-port=9527 --user-data-dir="F:\selenium\"') 或者这样打开新的环境





