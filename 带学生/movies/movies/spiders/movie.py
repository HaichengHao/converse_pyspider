import scrapy
from  ..items import MoviesItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://ssr1.scrape.center/"]
    model_url = 'https://ssr1.scrape.center/page/%d'
    page_num = 2
    def parse(self, response):
        # //div[contains(@class,"el-col")]//p[contains(@class,"score")]/text()
        card_all = response.xpath('//div[contains(@class,"el-col")]/div[contains(@class,"el-card")]')
        for card in card_all:

            # //div[contains(@class,"el-col")]/div[contains(@class,"el-card")]/div/div/div[2]/a/h2
            name = card.xpath('./div/div/div[2]/a/h2/text()').extract_first()
            # //div[contains(@class,"el-col")]/div[contains(@class,"el-card")]/div/div/div[3]/p[1]
            score = card.xpath('./div/div/div[3]/p[1]/text()').extract_first().strip()
            country_area = card.xpath('./div[@class="el-card__body"]/div/div[2]/div[2]/span[1]/text()').extract_first().strip()
            time_length = card.xpath('./div[@class="el-card__body"]/div/div[2]/div[2]/span[3]/text()').extract_first().strip()
            try:
                sysj = card.xpath('./div[@class="el-card__body"]/div/div[2]/div[3]/span/text()').extract_first().strip()
            except BaseException as e:
                sysj = ''

            print(name,score,country_area,time_length,sysj)

            item = MoviesItem()
            item['name'] = name
            item['score'] =score
            item['country_area'] = country_area
            item['time_length'] = time_length
            item['sysj'] = sysj

            yield item
        if self.page_num < 11:
            new_url = self.model_url %self.page_num
            self.page_num+=1
            yield scrapy.Request(url=new_url,callback=self.parse)

