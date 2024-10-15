# @Editor    : 百年
# @FileName  :04_selenium登录b站.py
# @Time      :2024/10/15 21:17
import time

from selenium.webdriver import Chrome
# 创建浏览器对象
browser1 = Chrome(executable_path='../others/chromedriver.exe')

# 获取b站的链接
url = 'https://www.bilibili.com/'
browser1.get(url)

# 定位到b站的登录按钮
login_btn = browser1.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div')

# 点击登录按钮
login_btn.click()

time.sleep(2)
# 定位到输入用户名的输入框
username_input = browser1.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/form/div[1]/input')

# 之后进行用户名的输入
usernm = input('输入你的用户名/账户>>')
username_input.send_keys(usernm)
time.sleep(1)
# 定位到输入密码的用户框
password_input = browser1.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/form/div[3]/input')
passwd = input('请输入密码:')
password_input.send_keys(passwd)
time.sleep(1)

# 定位到登录按钮并点击登录
dl_btn = browser1.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[2]/div[2]')
time.sleep(2)
dl_btn.click()

# 但是对于图形选文字验证码的确定并不能直接通过之前的动作链简单解决,
# 因为每次验证码需要点击的位置都不一样
# 所以我们需要用超级鹰这样的平台来做定位和点击

# selenium中心思想回顾:可见即可得
# 对于selenium不需要记住那么多属性

# 定位到完整的验证码对话框
ifrm = browser1.find_element_by_xpath('')
browser1.switch_to.frame(ifrm)

code_tag = browser1.find_element_by_xpath('/html/body/div[5]/div[2]/div[6]/div/div')
print(code_tag)

