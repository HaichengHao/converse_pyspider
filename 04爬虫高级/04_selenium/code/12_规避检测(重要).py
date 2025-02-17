# @Author    : 百年
# @FileName  :12_规避检测(重要).py
# @DateTime  :2024/10/21 13:25
'''
规避一些网站对于自动程序的封锁
如何判断,在网页打开调试界面找到console输入
window.navigator.webdriver
如果返回为undefined或false则表明该网页没使用selenium

尝试用selenium发送请求,并打开开发者工具
输入同样的代码，可以发现返回为true,说明我们被浏览器检测到了是自动化程序,所以我们目前要解决的问题是:
让网页不知道我们是自动化程序
'''
'''
那么如何解决?
实现js注入,绕过检测'''
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import Service
# 规避监测环节1
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
service = Service('../others/chromedriver.exe')
driver = Chrome(service=service, options=chrome_options)

# 规避环节2
#Selenium在打开任何页面之前，先运行这个Js文件。
with open('../others/stealth.min.js') as f:
    js = f.read()
#进行js注入，绕过检测
#execute_cdp_cmd执行cdp命令（在浏览器开发者工具中执行相关指令，完成相关操作）
#Page.addScriptToEvaluateOnNewDocument执行脚本
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

'''
注意:以上两个环节都可以规避监测,单独一个可能也可以,但是保险起见两个都上比较好
'''
# 访问淘宝
driver.get('https://www.taobao.com/')

'''
运行之后打开开发者工具,输入window.navigator.webdriver，发现已经不是true，而是变成了undefined'''