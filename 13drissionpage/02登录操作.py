# @Author    : 百年
# @FileName  :02登录操作.py
# @DateTime  :2025/5/30 19:18
from DrissionPage import ChromiumPage

#创建page对象并访问链接
page = ChromiumPage()
page.get('https://gitee.com/login?')

#定位到登录文本框获取文本框元素,注意这里携带是id选择器,结合前端知识理解
ele_login = page.ele('#user_login')

#传入数据到文本框中
ele_login.input('2020104216@qq.com')


#定位到密码输入文本框
ele_pwd = page.ele('#user_password')
pwd = input('请输入密码>>')
ele_pwd.input(pwd)

#定位到登录按钮
ele_login_btn = page.ele('@value=登 录')

#点击登录按钮
ele_login_btn.click()

#important:注意：ele()方法用于查找元素，它返回一个ChromiumElement对象，
# 用于操作元素。值得一提的是，ele()内置了等待，如果元素未加载，
# 它会执行等待，直到元素出现或到达时限。默认超时时间 10 秒。