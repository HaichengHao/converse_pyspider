import scrapy


class A1Spider(scrapy.Spider):
    name = "douban"
    # allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        # print(response.status)
        print(response.request.headers['User-Agent'])
        # print('被选定的代理',response.request.meta['proxy'])

