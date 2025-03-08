import scrapy


class DengluSpider(scrapy.Spider):
    name = "denglu"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.chaojiying.com/user/"]

    def parse(self, response):
        print(response.text)
