# @Author    : 百年
# @FileName  :06_规避检测之大火车.py
# @DateTime  :2024/10/22 17:04
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

# 创建浏览器配置信息
opts = Options()
opts.add_argument("--disable-blink-features=AutomationControlled")
opts.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
# 创建浏览器对象
browser1 = Chrome(executable_path='../others/chromedriver.exe', options=opts)

# 加载js代码,进行js注入
with open('../others/stealth.min.js') as f:
    js = f.read()

browser1.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

# 访问大火车

browser1.get('https://kyfw.12306.cn/otn/resources/login.html')

user_id = browser1.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input')
passwd = browser1.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input')
lg_btn = browser1.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/a')
# 点击id输入界面并输入id
user_id.click()
your_user_id = input('输入你的手机号>>')
user_id.send_keys(your_user_id)
time.sleep(1)
# 点击密码输入并输入密码
passwd.click()
your_passwd = input('输入你的密码>>')
passwd.send_keys(your_passwd)
time.sleep(1)

# 点击登录
lg_btn.click()
time.sleep(2)
# 接下来进行验证码输入
your_id4 = browser1.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div/div[1]/input')
your_id4.click()
youid4 = input('输入身份证后四位>>')
your_id4.send_keys(youid4)

time.sleep(2)  # 然后会发送验证码

# 点击获取验证码按钮
getvercode = browser1.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div/div[2]/a')
getvercode.click()

time.sleep(1)

verify_code = browser1.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div/div[2]/input')
verify_code.click()

# 交互输入验证码
youvercode = input('输入验证码>>')

verify_code.send_keys(youvercode)

time.sleep(1)
# 点击确定按钮
ack_btn = browser1.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div/div[4]/a')
ack_btn.click()
