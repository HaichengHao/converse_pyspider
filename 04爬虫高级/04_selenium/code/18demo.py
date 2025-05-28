"""
@File    :18demo.py
@Editor  : 百年
@Date    :2025/5/26 16:36 
"""

from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.bilibili.com/')
    # 获取远程链接的地址
    print('remote_url:', browser.caps['goog:chromeOptions']['debuggerAddress'])
    print('session_id:', browser.session_id)
    print(browser.title)

