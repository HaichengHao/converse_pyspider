import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        print(response.text)

