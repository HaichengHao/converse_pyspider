import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import CrawldemoItem
class JianliSpider(CrawlSpider):
    name = "jianli"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://sc.chinaz.com/jianli/"]
    link = LinkExtractor(allow=r"index_\d+\.html")
    # important:既然已经用上全站爬取了，可以再构造新的链接提取器来进行操作来获取详情页面的链接
    #  提取简历详情页的链接
    # link_detail = LinkExtractor(allow=r'//sc.chinaz.com/jianli/\d+\.htm')
    rules = (
        Rule(link, callback="parse_item", follow=False),
        # Rule(link_detail, callback="detail_parse") #important:再把新的规则加进去
    )

    def parse_item(self, response):
        # print(response)
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            title = div.xpath('.//p/a/text()').extract_first()
            link = div.xpath('.//p/a/@href').extract_first()
            item = CrawldemoItem()
            item['title'] = title
            item['link'] = link
            # print(title,link) #tips:检查一下是不是成功了
            yield scrapy.Request(url=link,callback=self.detail_parse,meta={'item': item})

    def detail_parse(self, response):
        item = response.meta['item']
        download_url = response.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href').extract_first()
        # print(download_url)
        item['download_url'] = download_url
        yield item

#important:纯cawlspider是无法进行请求传参的，异步获取的数据没办法进行数据匹配
# 所以我们需要结合起来手动发送请求使用，所以还是回归到了本来的思路

#runtime_result:
# {'download_url': 'https://downsc.chinaz.net/Files/DownLoad/jianli/202501/zji
# anli3555.rar',
#  'link': 'https://sc.chinaz.com/jianli/250125005340.htm',
#  'title': '5年经验酒店大堂经理求职简历模板'} 部分结果展示