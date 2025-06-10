"""
@File    :07完全使用自己的浏览器.py
@Editor  : 百年
@Date    :2025/6/5 8:50 
"""
from DrissionPage import ChromiumPage,ChromiumOptions

opts = ChromiumOptions().set_paths(user_data_path=r'D:\Chromeopts\data1')

page = ChromiumPage(addr_or_opts=opts)

page.get('https://sy.lianjia.com/ershoufang/')

all_a = page.eles('xpath://div[@data-role="ershoufang"]/div/a')
for a in all_a:
    #得到一整个市区的各个县的链接,之后发起访问
    print(a.link,a.text)

