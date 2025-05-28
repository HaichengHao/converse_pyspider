import scrapy


class LeziSpider(scrapy.Spider):
    name = "lezi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://domei.cn/wenan/27637.html"]

    def parse(self, response):
        # print(response.text)
        p_all = response.xpath('//div[@class="content"]/p[position()>2]') #定位到所有的p

        print(p_all)
        #注意xpath返回的类型
        for p in p_all:
            p = p.xpath('./text()').extract_first()
            print(p)
