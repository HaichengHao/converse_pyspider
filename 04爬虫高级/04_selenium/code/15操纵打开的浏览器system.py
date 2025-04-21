"""
@File    :15操纵打开的浏览器system.py
@Editor  : 百年
@Date    :2025/4/21 18:10 
"""
'''
这个也是两种写法,和popen差不多'''
# tips:写法1，start法
import os
os.system(r'start chrome --remote-debugging-port=9527')

# tips:写法2

os.chdir(r'C:\Program Files\Google\Chrome\Application')
os.system(r'start chrome --remote-debugging-port=9527')