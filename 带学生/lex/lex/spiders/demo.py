import scrapy
from scrapy.linkextractors import LinkExtractor

class DemoSpider(scrapy.Spider):
    name = "demo"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.wogif.com/duanzi/"]

    def parse(self, response):
        #创建链接提取器,写xpath定位的话就是到a标签
        le = LinkExtractor(restrict_xpaths='//div[@class="xxl-item"]/a')

        #利用链接提取器提取响应对象中满足xpath定位的链接
        a_lst = le.extract_links(response)
        for a in a_lst:
            #利用a.text可以获取a标签中的文本信息,利用.url可以获取链接信息
            print(a.text.strip(),a.url)

