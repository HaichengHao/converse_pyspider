# @Editor    : 百年
# @FileName  :08_基础补充.py
# @Time      :2024/10/7 20:55
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 构建浏览器
browser = Chrome(executable_path='../others/chromedriver.exe')

browser.get('https://www.jd.com/')

time.sleep(3)
# 定位到搜索栏
serach_input = browser.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/input')
# 输入搜索内容
serach_input.send_keys('轻薄本')
time.sleep(2)

# 点击搜索
btn = browser.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button')
btn.click()

time.sleep(2)

browser.switch_to.window(browser.window_handles[-1])
time.sleep(2)


# 执行js代码进行下滑
browser.execute_script(
    script="""
    document.documentElement.scrollTo(0,1000)
    """)
