"""
@File    :04cookie信息.py
@Editor  : 百年
@Date    :2025/7/3 20:07 
"""
from DrissionPage import SessionPage
page = SessionPage()

# cookies() 此方法返回 cookies 信息。


# 类型dict 和 list
page.get('https://www.baidu.com')
page.get('https://gitee.com')

# 最新版本才有as_dict
for i in page.cookies(all_domains=True,as_dict=False):
    print(i)