import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DailiSpider(CrawlSpider):
    name = "daili"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/ppt/index.html"]
    # tips: 链接提取器，可以根据指定的规则提取链接
    link = LinkExtractor(allow=r'index_\d+\.html') #important:注意这个.一定要加上\进行转义，不然其会匹配任意字符

    # tips: 规则就是参数allow表示的，allow后面跟的是正则表达式
    #  link对象可以根据allow表示的正则提取到符合正则要求的链接

    #tips:规则解析器
    # 该对象可以对link提取到的链接进行请求发送,根据指定规则解析请求到的页面源码数据
    # 此处的规则就是由callback参数来指定的
    rules = (Rule(link, callback="parse_item", follow=True),)
    #important:follow=True可以将链接提取器提取到的url依次作为起始url,即可将所有的页码链接全部取出

    #tips:数据解析
    # 改解析函数调用的次数取决于link提取链接的个数
    def parse_item(self, response):
        print(response)
