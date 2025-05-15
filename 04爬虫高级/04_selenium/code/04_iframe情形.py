# @Editor    : 百年
# @FileName  :04_iframe情形.py
# @Time      :2024/10/1 23:53
'''
有时候会出现iframe嵌套登录页面的场景,我们需要解决这个问题
默认的视频播放窗口中很多都是外层的一个html嵌套了一个iframe
我们在用selenium时候需要注意这一点,即需要将selenium的“视野”聚焦到iframe上
'''
# 先导入需要使用的包和模块
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#创建浏览器对象
service = Service('../../../练手/chromedriver.exe')
# browser1 = Chrome(executable_path='../others/chromedriver.exe')
browser1 = Chrome(service=service)

browser1.get('https://www.mjzj.me/vodplay/32236-1-1.html')

# 定位到iframe
# iframe = browser1.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td/iframe")
iframe = browser1.find_element(By.XPATH,"/html/body/main/div/div[2]/div[1]/div[1]/div/table/tbody/tr/td/iframe")
# important: 切换到iframe
time.sleep(4)
browser1.switch_to.frame(iframe)


time.sleep(3)
# 先定位到发送弹幕的input
# input_ = browser1.find_element_by_xpath("//input[@id='dmtext']")
input_ = browser1.find_element_by_xpath(By.XPATH,"//input[@id='dmtext']")
# 再通过这个input找到它的属性placeholder的属性值
place_holder = input_.get_property('placeholder')
place_holder2 = input_.get_attribute('placeholder') #这样写也是可以的

print(place_holder)

# 拿到之后我们现在想出来iframe
browser1.switch_to.parent_frame()

# 然后再拿在父框架的电影简介
time.sleep(2)
# 先定位
# movie_info = browser1.find_elements_by_xpath("//div[@class='ysinfo']")
# # 再打印
# print(type(movie_info))
# for item in movie_info:
#     print(item.text)

# 拿到关联推荐
# bind_rc = browser1.find_element_by_xpath("/html/body/main/div/div[3]/div[1]/h2")
bind_rc = browser1.find_element(By.XPATH,"/html/body/main/div/div[3]/div[1]/h2")
print(bind_rc.text)