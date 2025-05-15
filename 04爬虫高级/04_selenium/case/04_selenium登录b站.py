# @Editor    : 百年
# @FileName  :04_selenium登录b站.py
# @Time      :2024/10/15 21:17
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 导入Options类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--force-device-scale-factor=1')  # 强制缩放比例为100%
options.add_argument('--window-size=1920,1080')  # 固定窗口大小

service = Service('../others/chromedriver.exe')
browser1 = Chrome(service=service, options=options)

# 获取b站的链接
url = 'https://www.bilibili.com/'
browser1.get(url)

# 定位到b站的登录按钮
# login_btn = browser1.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div')
login_btn = browser1.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div')


# 点击登录按钮
login_btn.click()

time.sleep(2)
# 定位到输入用户名的输入框
username_input = browser1.find_element(By.XPATH,'/html/body/div[4]/div/div[4]/div[2]/form/div[1]/input')

# 之后进行用户名的输入
usernm = input('输入你的用户名/账户>>')
username_input.send_keys(usernm)
time.sleep(1)
# 定位到输入密码的用户框
password_input = browser1.find_element(By.XPATH,'/html/body/div[4]/div/div[4]/div[2]/form/div[3]/input')
passwd = input('请输入密码:')
password_input.send_keys(passwd)
time.sleep(2)

# 定位到登录按钮并点击登录
dl_btn = browser1.find_element(By.XPATH,'/html/body/div[4]/div/div[4]/div[2]/div[2]/div[2]')
time.sleep(2)
dl_btn.click()

# 但是对于图形选文字验证码的确定并不能直接通过之前的动作链简单解决,
# 因为每次验证码需要点击的位置都不一样
# 所以我们需要用超级鹰这样的平台来做定位和点击

# selenium中心思想回顾:可见即可得
# 对于selenium不需要记住那么多属性

# 定位到完整的验证码对话框
time.sleep(3)
# code_tag = browser1.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[6]/div/div')
# code_tag = WebDriverWait(browser1, 20).until(
#     EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div[6]/div/div'))
# )
# 等待验证码容器出现（Geetest 验证码面板）
code_tag = WebDriverWait(browser1, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.geetest_panel_next'))
)
print(code_tag)
print("验证码元素大小:", code_tag.size)
print("验证码元素位置:", code_tag.location)
# code_tag.screenshot('../others/code.png')

# time.sleep(6)
# # 识别验证码(使用打码平台进行验证码识别)
# # 然后定位到图片,直接将图片作为png格式,对比学习之前的使用回顾,selenium在某些方面还是有点方便的
im = code_tag.screenshot_as_png  # 我们直接调用将其保存成功图片
chaojiying = Chaojiying_Client('minkofox', 'HHCzio20.', '963713')
result = chaojiying.PostPic(im, 9004)

# print(result['pic_str'])
print(result)
'''
{'err_no': 0, 'err_str': 'OK', 
'pic_id': '1266120541083430028', 
'pic_str': '214,209|133,170|254,89|60,234',
 'md5': 'ce0580f7b163af15f5be1623b07a50f9'}'''
# 切分坐标,注意,切分的返回值是一个列表
code_xy = result['pic_str'].split('|')
print(code_xy)
# # 创建动作链
for pos in code_xy:
    print("当前验证码元素位置:", code_tag.location)
    time.sleep(1)
    pos_lst = pos.split(',')  # 利用逗号切分xy,返回的是x,y坐标组成的列表
    print(pos_lst)
    # 注意还需要将其强转为整数类型
    x = int(pos_lst[0])
    y = int(pos_lst[1])
    # adjusted_x = x - code_tag.location['x']
    # adjusted_y = y - code_tag.location['y']
    # ActionChains(browser1).move_to_element_with_offset(code_tag, adjusted_x, adjusted_y).click().perform()

    time.sleep(2)  # 给验证码充分的时间加载和稳定下来
    ActionChains(browser1).move_to_element_with_offset(code_tag, x, y).click().perform()
    time.sleep(1)
# for pos in code_xy:
#     time.sleep(1)
#     pos_lst = pos.split(',') #利用逗号切分xy,返回的是x,y坐标组成的列表
#     print(pos_lst)
#     # 注意还需要将其强转为整数类型
#     x = int(pos_lst[0])
#     y = int(pos_lst[1])
#     # 让动作链来点击定位到的坐标，并点击
#     # 注意这里用的不是move_by_offset,因为其是根据整个屏幕左下角来作为起始点的
#     # 而move_to_element_offset是以我们指定的element标签为起始点的
#     # 这个例子中我们是以定位到的验证码图片标签的左下角为坐标原点的
#     ActionChains(browser1).move_to_element_with_offset(to_element=code_tag,xoffset=x,yoffset=y).click().perform()
#
# time.sleep(1)

# 点击确认按钮

# su_btn = browser1.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[6]/div/div/div[3]/a')

# su_btn.click()
