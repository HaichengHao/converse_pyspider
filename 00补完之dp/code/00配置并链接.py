"""
@File    :00配置并链接.py
@Editor  : 百年
@Date    :2025/6/6 21:23 
"""
from DrissionPage import Chromium,ChromiumOptions

#创建浏览器对象,指定浏览器路径
chrome_opts = ChromiumOptions().set_browser_path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

#用该配置创建页面对象
bro = Chromium(addr_or_opts=chrome_opts)
#然后利用该bro创建页面对象
page = bro.latest_tab
page.get('https://www.baidu.com')
