import scrapy


class MidwSpider(scrapy.Spider):
    name = "midw"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print(response.text)
