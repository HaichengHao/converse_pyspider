"""
@File    :00初体验.py
@Editor  : 百年
@Date    :2025/6/3 10:17 
"""
import time

from DrissionPage import WebPage

page = WebPage()
#
page.get('https://sy.lianjia.com/')

login = page.ele('xpath://span[@class="reg"]')
login.click()
login_bypwd = page.ele('xpath://li[@data-type="1"]')
login_bypwd.click()

id_input = page.ele('xpath:/html/body/div[22]/div[2]/div[2]/div[4]/div[2]/form[2]/ul/li[1]/input')
#清理
id_input.clear()
id_input.input('18864771568')

pwd_input = page.ele('.password_type password_input')
pwd_input.input('HHCzio20')


#点击登录按钮
login_btn = page.ele('xpath:/html/body/div[22]/div[2]/div[2]/div[4]/div[2]/form[2]/div[2]')
login_btn.click()



time.sleep(5)
#切换为session mode,实现requests那样的访问形式
page.change_mode()
page.get(url='https://sy.lianjia.com/ershoufang/')
print(page.html)