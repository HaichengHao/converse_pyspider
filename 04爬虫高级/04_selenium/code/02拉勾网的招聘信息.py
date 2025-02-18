# @Editor    : 百年
# @FileName  :02拉勾网的招聘信息.py
# @Time      :2024/9/29 22:55
# tips:全部关于selenium的都用新的语法规则替换
import time  # 如果有时候操作叠加过快,那就手动设置timesleep来控制时间,直接进行sleep操作
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from requests import Session

# chdr_path = '../others/chromedriver.exe'
# 创建一个Chrome对象
# web = Chrome(executable_path=chdr_path)
service = Service('../others/chromedriver.exe')
web = Chrome(service=service)
# 访问拉勾网
web.get(url='https://www.lagou.com/wn/')

# 找到关注公众号的x并点击它
# 我们根据xpath定位到我们要关闭的按钮
# close_btn = web.find_element_by_xpath("//img[@class='app-down-close']")
# 点击关闭按钮,其实结合js的一些知识可以更好学习这一部分
# close_btn.click()
time.sleep(2)
# 利用selenium能够动态执行Js的功能调用js代码,将下方无法关闭的横幅广告关闭掉
web.execute_script("""
let ad = document.getElementsByClassName('loginBar__3S_rT')[0];
ad.parentNode.removeChild(ad);
""")
time.sleep(2)
# 点击进行登录的按钮
# jxdl = web.find_element_by_xpath("/html/body/div[1]/header/div[1]/div[2]/ul/li[1]/a")
jxdl = web.find_element(By.XPATH,"/html/body/div[1]/header/div[1]/div[2]/ul/li[1]/a")

# 点击
jxdl.click()


time.sleep(5)
# 注意现在已经相当于换了一个页面,不能按照人类的逻辑来揣测selenium的逻辑
# 对于是否发生页面的变化,直接看url栏里的链接有没有发生变化就知道了
# 利用密码登录
time.sleep(5)
# 我们需要转换窗口
# web.switch_to.window(web.window_handles[-1])
# kwlg = web.find_element_by_xpath("//div[@class='sc-fotOHu fLmipN']//div[@class='sc-ezbkAF bUNcAS']")
kwlg = web.find_element(By.XPATH,"//div[@class='sc-fotOHu fLmipN']//div[@class='sc-ezbkAF bUNcAS']")
time.sleep(5)
kwlg.click() #点击使用密码登录
time.sleep(3)
# 输入手机号
# phone_number = web.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/input")
phone_number = web.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/input")
# 传入手机号
phone_number.send_keys(input('输入手机号:'))

# 输入密码
# kd = web.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/input")
kd = web.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/input")
# 传入密码
kd.send_keys(input('输入密码'))

time.sleep(2)

# 点击同意协议
# tyxy  = web.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div")
tyxy  = web.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div")
tyxy.click()
time.sleep(3)
# 登录
# 点击登录按钮进行登录
# login = web.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/button/span")
login = web.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/button/span")
login.click()

# 注意,要进行quit()操作,这是最完整的

# 浏览器.quit

# 那么就进行这一步操作
web.quit()


