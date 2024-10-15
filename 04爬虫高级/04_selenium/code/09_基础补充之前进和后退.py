# @Editor    : 百年
# @FileName  :09_基础补充之前进和后退.py
# @Time      :2024/10/15 20:27
import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options
# opts=Options()
# opts.add_argument('--headless')
# opts.add_argument('--disable-gpu')

# 创建浏览器对象
browser1 = Chrome(executable_path='../others/chromedriver.exe')

# 获取页面数据
browser1.get(url='https://ypk.39.net/ganmao/k1')

time.sleep(2)
# 点击下一页
nxt_btn = browser1.find_element_by_xpath('/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div/p/a[6]')
nxt_btn.click()
time.sleep(2)
# 点击返回上一页,即后退
browser1.back()

time.sleep(2)
# 回到刚才没后退的那一页
browser1.forward()

time.sleep(4)
browser1.quit()