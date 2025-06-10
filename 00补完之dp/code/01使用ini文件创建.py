"""
@File    :01使用ini文件创建.py
@Editor  : 百年
@Date    :2025/6/6 21:35 
"""

'''important: 其实可以发现一个特点
那就是新版本中使用的Chromium比之前的ChromiumPage多了创建浏览器这一步
之前是page = ChromiumPage()  
page.get()
 现在是   
 bro = Chromium()  
 page = bro.latest_tab
 page.get()
 '''
from DrissionPage import Chromium,ChromiumOptions

#创建配置对象时指定要读取的ini文件路径
chrome_option = ChromiumOptions(ini_path=r'./myconfig1.ini')

#使用该配置对象创建页面对象
browser = Chromium(addr_or_opts=chrome_option)
