# @Author    : 百年
# @FileName  :04模式切换.py
# @DateTime  :2025/5/30 19:50

'''
这个示例演示WebPage如何切换控制浏览器和收发数据包两种模式。
通常，切换模式是用来应付登录检查很严格的网站，
可以用控制浏览器的形式处理登录，再转换模式用收发数据包的形式来采集数据。
'''

from DrissionPage import WebPage,ChromiumPage

#创建页面对象
page = WebPage()
#访问网址进行登录
page.get('https://gitee.com/login?')

#定位到登录文本框获取文本框元素,注意这里携带是id选择器,结合前端知识理解
ele_login = page.ele('#user_login').clear()

#传入数据到文本框中
ele_login.input('2020104216@qq.com')


#定位到密码输入文本框,先清空
ele_pwd = page.ele('#user_password').clear()
pwd = input('请输入密码>>')
ele_pwd.input(pwd)

#定位到登录按钮
ele_login_btn = page.ele('@value=登 录')

#点击登录按钮
ele_login_btn.click()

#切换到收发数据包的模式
page.change_mode() #切换的时候程序会在新模式重新访问当前的url
#访问我的主页
page.get('https://gitee.com/muguilin',timeout=2)

# 根据class属性值获取div标签，然后将该div下面class为item的元素标签批量获取
items = page.ele('.ui middle aligned list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('.content').text)