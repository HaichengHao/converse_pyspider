import scrapy


class MidWareSpider(scrapy.Spider):
    name = "mid_ware"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://cn.bing.com/",'https://flowus.cn/product']
    proxy_lst=[] #tips:先创建个代理列表用于接收付费代理api返回的代理信息
    def parse(self, response):
        # print(response)
        # important：假设有购买付费代理，直接想要调用api,那么可以这样做
        proxy_url = 'xxx'