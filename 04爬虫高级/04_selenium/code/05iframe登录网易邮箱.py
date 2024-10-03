# @Editor    : 百年
# @FileName  :05iframe登录网易邮箱.py
# @Time      :2024/10/3 10:50
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver import Chrome
import time

# 1. 创建一个ChromeDriver
driver = Chrome(executable_path='../others/chromedriver.exe')

# 2. 获取网易邮箱的地址
driver.get('https://www.126.com/')

# 3. 定位到iframe
login_iframe = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div/div[3]/div[1]/div[2]/iframe")

# 4. 切换到iframe
driver.switch_to.frame(login_iframe)

# 5.定位到输入邮箱的界面
mailcode = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input")
time.sleep(1)
mailcode.send_keys('jntm25years')

# 6.退出iframe
driver.switch_to.parent_frame()

# 7.获取父框架中的内容
p1 = driver.find_elements_by_xpath("/html/body/div[2]/p")
print(p1[0].text)