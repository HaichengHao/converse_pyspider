import scrapy


class MidwSpider(scrapy.Spider):
    name = "midw"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print(response.text)
'''Runtime_result 
我是spider_opened
我是proecess_request
我是proecess_request2
我是process_reqponse2
我是process_reqponse
'''