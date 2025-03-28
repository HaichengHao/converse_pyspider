# """
# @File    :国密sm2.py
# @Editor  : 百年
# @Date    :2025/3/27 16:36
# """
# import execjs
#
# # step 1 创建node对象
# node = execjs.get()
# # step 2 编译js文件返回上下文对象
# with open('cfw_sm2.js','r',encoding='utf-8') as fp:
#     ctx = node.compile(fp.read())
#
# funcname = 'getPwd_sm2("123456")'
# result = ctx.eval(funcname)
# print(result)


"""
@File    : 国密sm2.py
@Editor  : 百年
@Date    : 2025/3/27 16:36
"""
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Step 1: 配置 ChromeDriver 路径
# 确保你已经安装了 ChromeDriver，并将其路径替换为实际路径
chrome_driver_path = "E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe"  # 替换为你的 chromedriver 路径

# 创建 WebDriver 对象
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Step 2: 打开空白页面
    driver.get("about:blank")

    # Step 3: 读取 JavaScript 文件内容
    with open('cfw_sm2.js', 'r', encoding='utf-8') as fp:
        js_code = fp.read()

    # Step 4: 在浏览器中执行 JavaScript 文件内容
    driver.execute_script(js_code)

    # Step 5: 调用 JavaScript 函数并获取结果
    funcname = 'getPwd_sm2("123456")'  # 替换为你要调用的函数
    result = driver.execute_script(f"return {funcname};")
    print("Result:", result)

finally:
    # Step 6: 关闭浏览器
    time.sleep(2)  # 等待一段时间，确保结果正确输出
    driver.quit()