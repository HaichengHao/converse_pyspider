import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from ..items import WangyiproItem
service = Service('E:/converse_spider/converse_pyspider/06scrapy/chromedriver.exe')

#tips: xpath路径
#   //div[@class='ns_area list']/ul/li[position()>1]/a/@href
class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]
    model_urls =[] #important:创建一个列表用于存储详情页的的url#
    # tips:创建浏览器对象，因为作为类变量的话好访问
    browser = Chrome(service=service)
    def parse(self, response):
        model_index = [2,3,5,6]
        li_list = response.xpath("//div[@class='ns_area list']/ul/li")
        # tips:遍历model_index将我们要爬取的数据(国内,国际,军事,航空获取到对应的页面的url)
        for ix in model_index:
            model_url = li_list[ix-1].xpath("./a/@href").extract_first()
            self.model_urls.append(model_url)
        # print(li_list)
        print(self.model_urls)
        # tips:拿到详情页的链接之后就是对详情页面发送请求
        for model_url in self.model_urls:
            yield scrapy.Request(url=model_url,callback=self.parse_detail)
    def parse_detail(self,response):
        # tips:因为网页是动态加载的，所以我们需要使用selenium进行动态请求
        # important:刚才在middlewares中将动态加载的response也处理好了，所以可以安心的做解析了
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            try:
                # 解析新闻标题
                title = div.xpath('./div/div/h3/a/text()').extract_first()
                detail_href = div.xpath('./a/@href').extract_first()
                item=WangyiproItem()
                item['title'] = title
                # 新闻详情页链接
            except Exception as e:
                print('遇到广告已忽略!',e)

            # 接下来需要对新闻的详情页发起请求
            if detail_href !=None:
                # important:请求传参，将item传给newscontent_parse
                yield scrapy.Request(meta={'item':item},url=detail_href,callback=self.newscontent_parse)
    # important:解析新闻详情页的内容
    def newscontent_parse(self,response):
        item = response.meta['item']
        # 获取每一页新闻的内容
        content = response.xpath('//div[@class="post_body"]//text()').extract() #important:注意，xpath返回的是列表，
        # 所以我们还需要将这个列表拼接回字符串
        content = ''.join(content).strip() #将列表拼接回字符串并且去除左右的空格
        item['content'] = content
        yield item

    # 重写一个父类方法叫close_spider改方法只会在爬虫结束后执行一次
    def close(self,spider):
        print('关闭浏览器成功')
        self.browser.quit()