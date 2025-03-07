import scrapy

# important:学习本节时，对比之前的imgpro进行学习



class BizhiSpider(scrapy.Spider):
    name = "bizhi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://bz.zhongerqiqi.cn/#/"]


    def parse(self, response):
        print(response.text)
