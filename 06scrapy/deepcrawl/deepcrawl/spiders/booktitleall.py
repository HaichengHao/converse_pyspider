import scrapy
from ..items import DeepcrawlItem

class BooktitleallSpider(scrapy.Spider):
    # important: 类属性
    name = "booktitleall"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.shuqi.com/store?spm=aliwx.pc-web-bookstore.0.0"]
                # https://www.shuqi.com/store?spm=aliwx.list_store.0.0&page=2
    url_model = "https://www.shuqi.com/store?spm=aliwx.list_store.0.0&page=%d"
    page_number = 2 #tips: 定义类属性page_number，用于我们进行多页爬取的页数的初始化
    def parse(self, response):
        li_lst = response.xpath('//ul[@class="store-ul clear"]/li')
        for li in li_lst:
            img_src = li.xpath('./a/img/@src').extract_first()
            booktitle=li.xpath('./a/h3').extract_first().replace('<h3>','').replace('</h3>','')
            author = li.xpath('./p/a').extract_first().split('：')[-1].split('<')[0]
            category = li.xpath('./p/span/text()').extract_first()
            abstract = li.xpath('./a[2]/p').extract_first().split('>')[1].split('<')[0]
            # print(booktitle)
            # print(author)
            # print(category)
            # print(abstract)
            # print(img_src)
        #     important:实例化item对象
            item = DeepcrawlItem()
            item['img_src'] = img_src
            item['booktitle']=booktitle
            item['author']=author
            item['category']=category
            item['abstract']=abstract
            yield item
        if self.page_number < 6: #tips:结束递归的条件，只爬取前五页
            new_url = self.url_model %self.page_number
            self.page_number+=1 #然后让page_number+1
            # 手动请求发送
            yield scrapy.Request(url=new_url,callback=self.parse)
            #important:程序设计逻辑
            # 对生成的新的url发送请求，然后添加回调函数，回调函数利用的就是我们解析数据用的实例方法self.parse
