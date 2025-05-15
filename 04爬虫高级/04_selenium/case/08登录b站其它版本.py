"""
@File    :08登录b站其它版本.py
@Editor  : 百年
@Date    :2025/5/15 22:08 
"""
# @Editor    : 百年
# @FileName  : 04_selenium登录b站.py
# @Time      : 2024/10/15 21:17

import time
from chaojiying import Chaojiying_Client
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置浏览器选项
options = Options()
options.add_argument('--force-device-scale-factor=1')  # 强制缩放比例为100%
options.add_argument('--window-size=1920,1080')  # 固定窗口大小

service = Service('../others/chromedriver.exe')
browser1 = Chrome(service=service, options=options)

# 打开B站首页
url = 'https://www.bilibili.com/'
browser1.get(url)

# 等待并点击登录按钮（使用CSS选择器）
login_btn = WebDriverWait(browser1, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.header-login-entry'))
)
login_btn.click()

# 等待用户名输入框出现并输入用户名
username_input = WebDriverWait(browser1, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.bili-mini-account input'))
)
usernm = input('输入你的用户名/账户>>')
username_input.send_keys(usernm)

# 输入密码
password_input = WebDriverWait(browser1, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.bili-mini-password input'))
)
passwd = input('请输入密码:')
password_input.send_keys(passwd)

# 点击登录按钮
dl_btn = WebDriverWait(browser1, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-login'))
)
dl_btn.click()

# 等待验证码容器出现（Geetest 验证码面板）
code_tag = WebDriverWait(browser1, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.geetest_panel_next'))
)
print("验证码元素大小:", code_tag.size)
print("验证码元素位置:", code_tag.location)

# 截图验证码区域
im = code_tag.screenshot_as_png
chaojiying = Chaojiying_Client('minkofox', 'HHCzio20.', '963713')
result = chaojiying.PostPic(im, 9004)

print(result)
code_xy = result['pic_str'].split('|')
print(code_xy)

# 创建动作链点击每个坐标点
for pos in code_xy:
    time.sleep(1)
    x, y = map(int, pos.split(','))
    adjusted_x = x - code_tag.location['x']
    adjusted_y = y - code_tag.location['y']
    ActionChains(browser1).move_to_element_with_offset(code_tag, adjusted_x, adjusted_y).click().perform()
    time.sleep(1)

# 点击确认按钮
su_btn = WebDriverWait(browser1, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.geetest_commit_tip a'))
)
su_btn.click()