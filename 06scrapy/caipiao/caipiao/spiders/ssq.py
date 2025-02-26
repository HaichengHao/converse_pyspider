import scrapy






class SsqSpider(scrapy.Spider):
    name = "ssq"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://datachart.500.com/ssq/"]
    def parse(self, response):
        tr_lst = response.xpath('//*[@id="tdata"]/tr')
        for tr in tr_lst:
            if tr.xpath("./@class").extract_first() == "tdbck":
                continue
            date = tr.xpath('./td[1]').extract_first()
            red_ball = tr.xpath('./td[@class="chartBall01"]/text()').extract()
            blue_ball = tr.xpath('./td[@class="chartBall01 chartBall07"]').extract()
            # important:scrapy支持xpath和css混合使用
            # red_ball = tr.css(".chartBall01::text").extract() #这里就是使用了类选择器
            print(red_ball)
            # dic = {
            #     'qihao':date,
            #     'red_ball':red_ball,
            #     'blue_ball':blue_ball
            # }
            # yield dic #tips:将会对其传入管道
