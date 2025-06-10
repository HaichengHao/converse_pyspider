"""
@File    :02多浏览器共存.py
@Editor  : 百年
@Date    :2025/6/1 16:20 
"""
from DrissionPage import ChromiumPage,ChromiumOptions

#创建多个配置对象,每个指定不同的端口号和用户文件夹路径

opt1 = ChromiumOptions().set_paths(local_port=9111,user_data_path=r'D:\Chromeopts\data1')
opt2 = ChromiumOptions().set_paths(local_port=9119,user_data_path=r'D:\Chromeopts\data2')

#创建多个页面对象
page1 = ChromiumPage(addr_or_opts=opt1)
page2 = ChromiumPage(addr_or_opts=opt2)

#每个页面对象控制一个浏览器
page1.get('https://www.baidu.com')
page2.get('https://bilibili.com')