"""
@File    :16操纵打开的浏览器subprocess法.py
@Editor  : 百年
@Date    :2025/4/21 18:16 
"""
import os
import subprocess
os.chdir(r'C:\Program Files\Google\Chrome\Application')
subprocess.Popen('chrome.exe --remote-debugging-port=9527')