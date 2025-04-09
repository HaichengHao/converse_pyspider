import scrapy


class MingdanSpider(scrapy.Spider):
    name = "mingdan"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.dxsbb.com/news/64928.html"]

    def parse(self, response):
        tr_lst = response.xpath('//tbody/tr[position()>1]')
        for tr in tr_lst:
            rank = tr.xpath('./td[1]/text()').extract_first()
            scname = tr.xpath('./td[2]/text()').extract_first()
            place = tr.xpath('./td[3]/text()').extract_first()
            print(rank,scname,place)
