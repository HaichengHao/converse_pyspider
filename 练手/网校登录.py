# @Author    : 百年
# @FileName  :网校登录.py
# @DateTime  :2025/5/13 20:31
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from lxml import etree

service = Service('./chromedriver.exe')

bro1 = Chrome(service=service)

bro1.get('https://ks.wangxiao.cn/')
time.sleep(2)
loginbtn = bro1.find_element(By.XPATH,'//div[@class="topTools__temp"]/a[1]')
loginbtn.click()
time.sleep(2)
log_by_pwd = bro1.find_element(By.XPATH,'//div[@id="tab-click"]/div[3]')
log_by_pwd.click()
time.sleep(1)
tel_input = bro1.find_element(By.XPATH,'//div[@id = "normal-login"]/div[@class="tel"]/input[@id="username"]')
tel_input.click()
tel_input.send_keys("1886471568")
ncode_input = bro1.find_element(By.XPATH,'//div[@id = "nimg-code"]/div[@class="left"]/input[@id="ncode"]')
ncode = input('输入验证码>>')
ncode_input.send_keys(ncode)

pwd = input("输入密码>>")
passwd_input = bro1.find_element(By.XPATH,'//div[@class="password"]/input[@id="pwd"]')

passwd_input.send_keys(pwd)

login_now = bro1.find_element(By.XPATH,'//div[@id="login-normal"]')
login_now.click()

time.sleep(2)
cookies_me = bro1.get_cookies()
print(cookies_me)