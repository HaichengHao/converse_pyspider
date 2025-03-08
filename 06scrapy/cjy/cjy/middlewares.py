# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#
#
# import base64
import json
import time

import requests
from scrapy import signals
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

#
# class CjyDownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def spider_opened(self, spider):
#         spider.logger.info("Spider opened: %s" % spider.name)
#         service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')
#         bro = Chrome(service=service)
#         bro.get(url='https://www.chaojiying.com/user/login/')
#         bro.find_element(By.XPATH, '//input[@name="user"]').send_keys('minkofox')
#         bro.find_element(By.XPATH, '//input[@name="pass"]').send_keys('HHCzio20.')
#         img = bro.find_element(By.XPATH, '//input[@name="imgtxt"]')
#         lgbtn = bro.find_element(By.XPATH, '//input[@class="login_form_input_submit"]')
#         # usrname = input('请输入用户名>>')
#         # passwd = input('请输入密码>>')
#         # vcode = input('请输入验证码>>')
#         # usr.send_keys(usrname)
#         # pwd.send_keys(passwd)
#         # imgtxt.send_keys(vcode)
#         # img.screenshot_as_base64,可以将图片保存为b64类型
#         vcode = self.base64_api('minkofox','HHCzio20.',img.screenshot_as_base64,3)
#         img.send_keys(vcode)
#         lgbtn.click()
#         time.sleep(4)
#         # self.bro.get_cookies() #获取到cookies,注意之前学的shujia,selenium获取的cookies和传入的cookie都是有特定的格式的
#         # 并且是键值对组成的一个列表
#         self.cookie = {item['name']:item['value'] for item in bro.get_cookies()}
#
#     def process_request(self, request, spider):
#         if not request.cookies:
#             request.cookies = self.cookie
#             # page_source = self.bro.page_source
#             # return HtmlResponse(
#             #     url='https://www.chaojiying.com/user/login/',
#             #     request=request,
#             #     body=page_source,
#             #     encoding='utf-8'
#             # )
#         else:
#             return None
#
#     # def base64_api(uname, pwd,image,typeid):
#     #     data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#     #     result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#     #     if result['success']:
#     #         return result["data"]["result"]
#     #     else:
#     #         # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
#     #         return result["message"]
#     #     return ""
#
#     def base64_api(uname, pwd, b64, typeid):
#         data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#         result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#         if result['success']:
#             return result["data"]["result"]
#         else:
#             # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
#             return result["message"]
#         return ""


class CjyDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        try:
            spider.logger.info("Spider opened: %s" % spider.name)
            service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')
            bro = Chrome(service=service)
            bro.get(url='https://www.chaojiying.com/user/login/')
            time.sleep(3)
            bro.find_element(By.XPATH, '//input[@name="user"]').send_keys('minkofox')
            bro.find_element(By.XPATH, '//input[@name="pass"]').send_keys('HHCzio20.')
            img = bro.find_element(By.XPATH, '//input[@name="imgtxt"]')
            lgbtn = bro.find_element(By.XPATH, '//input[@class="login_form_input_submit"]')

            # vcode = self.base64_api('minkofox', 'HHCzio20', img.screenshot_as_base64, typeid=3)
            vcode = input('请输入验证码>>')
            img.send_keys(vcode)
            time.sleep(2)  # 等待验证码识别
            # img.send_keys(vcode)

            time.sleep(4)
            lgbtn.click()
            self.cookie = {item['name']: item['value'] for item in bro.get_cookies()}
            self.page_source = bro.page_source
        except Exception as e:
            spider.logger.error(f"Error during login: {e}")
            self.cookie = {}  # 或者根据实际情况提供默认值或处理方式

    def process_request(self, request, spider):
        if not request.cookies and hasattr(self, 'cookie'):
            request.cookies = self.cookie
            page_source = self.page_source
            return HtmlResponse(
                url='https://www.chaojiying.com/user/login/',
                request=request,
                body=page_source,
                encoding='utf-8'
            )
        else:
            return None

    def base64_api(self, uname, pwd, b64, typeid):
        data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        print(result)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        # return ""