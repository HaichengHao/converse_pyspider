import scrapy
from boss.request import SeleniumRequest
from ..items import BossItem


class ZhipinSpider(scrapy.Spider):
    page_number = 1
    name = "zhipin"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=&city=101070100&position=100109"]
    model_url ="https://www.zhipin.com/web/geek/job?query=&city=101070100&position=100109&page=%d"
    #important:对初始请求方法进行重写
    def start_requests(self): #important:注意这里的改写父类的start_requests方法，不要拼写错误，否则会导致不能正确运行，会当成普通请求不走selenium
        print('开始了请求!!!')
        yield SeleniumRequest( #important: 将起始的请求封装成属于SeleniumRequest类的请求
            url=self.start_urls[0],
            callback=self.parse
        )
        # yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        div_lst = response.xpath('//ul[@class="job-list-box"]/li/div[@class="job-card-body clearfix"]')
        for div in div_lst:
            # print('processing_div',div.get())
            jobname = div.xpath('./a/div/span[@class="job-name"]/text()').extract_first()
            jobarea = div.xpath('./a/div//span[@class="job-area"]/text()').extract_first()
            salary = div.xpath('./a/div/span[@class="salary"]/text()').extract_first()
            item = BossItem()
            item['job_name'] = jobname
            item['job_area'] = jobarea
            item['salary'] = salary
            yield item
        if self.page_number <= 3:

            next_page_url = self.model_url % self.page_number
            print('开始了请求!!!:', next_page_url)
            self.page_number += 1
            yield SeleniumRequest(
                url=next_page_url,
                callback=self.parse
            )
            # yield scrapy.Request(url=next_page_url, callback=self.parse)