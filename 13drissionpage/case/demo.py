"""
@File    :demo.py
@Editor  : 百年孤独
@Date    :2025/7/18 11:48 
"""
import time

from DrissionPage import WebPage

page = WebPage()
page.get('https://i-hn.meiyijia.com.cn/login.html?ReturnUrl=%2f')
logininput = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/input')
logininput.clear()
logininput.input('13349925309')
pwdinput = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[4]/input')
pwdinput.clear()
pwdinput.input('13477062863Czk')
verify_code = input('请输入验证码>>>')
verify_code_input = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[6]/input')
verify_code_input.clear()
verify_code_input.input(verify_code)

lg_btn = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[8]/button')
lg_btn.click()
time.sleep(4)

# 访问想访问的那个
page.get('https://i-hn.meiyijia.com.cn/#/StockAccount',timeout=2) #设置两秒让它加崽一下
print(page.html)
