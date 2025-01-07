import scrapy


class DpproSpider(scrapy.Spider):
    name = "dppro"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://ypk.39.net/pifu/p3/"]

    def parse(self, response):
        title = response.xpath('//p[@class="drugs-ul-tit"]/a').extract_first()
        print(title)
