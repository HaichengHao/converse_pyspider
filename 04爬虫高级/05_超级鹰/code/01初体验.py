# @Editor    : 百年
# @FileName  :01初体验.py
# @Time      :2024/10/6 20:02

'''
用超级鹰登录超级鹰
'''
import time

from chaojiying import Chaojiying_Client
from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# 设置无头浏览器
# Opts = Options()
# Opts.add_argument(
#     '--disable-gpu'
# )
# Opts.add_argument(
#     '--headless'
# )
# 创建一个浏览器对象
browser1 = Chrome(executable_path='../../04_selenium/others/chromedriver.exe')

# 获取链接
browser1.get(url='https://www.chaojiying.com/user/login')

time.sleep(2)
# 先定位到用户名的输入框
user_name = browser1.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input')
user_name.send_keys('minkofox')

time.sleep(3)

# 再定位到输入密码的框
passwd = browser1.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input')
passwd.send_keys('HHCzio20.')

time.sleep(2)

# 然后定位到图片,直接将图片作为png格式,对比学习之前的使用回顾,selenium在某些方面还是有点方便的
im = browser1.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png #我们直接调用将其保存成功图片
chaojiying=Chaojiying_Client('minkofox','HHCzio20.','963713')
result=chaojiying.PostPic(im,1004)

print(result)
print(result['pic_str'])
# 然后再定位到验证码输入框,将得到的验证码输入进去
ver_code = browser1.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input')

ver_code.send_keys(result['pic_str'])

time.sleep(3)
# 之后定位到登录按钮并点击登录
login = browser1.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input')

# 点击
login.click()
