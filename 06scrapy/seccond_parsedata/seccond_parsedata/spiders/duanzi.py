import scrapy


class DuanziSpider(scrapy.Spider):
    name = "duanzi"
    # allowed_domains = ["www.xxx.com"]

    # tips:对首页进行网络请求
    # scrapy会对列表中的url发起get请求
    start_urls = ["https://www.wogif.com/duanzi/"]

    def parse(self, response):
        #QUIZ:如何获取响应数据
        #ANSWER:直接使用xpath方法结合xpath语法格式即可对response中的数据进行数据解析
        # tips:先获取最外层的标签
        divlst = response.xpath('//div[@class="xxl-item"]/a/div')
        # print(divlst)
        # 然后用做成的新的对象divlst去寻找它内部的标签，这一点有些像pyquery
        for div in divlst:
            # title = div.xpath('./h2')[0].extract().replace('<h2>','').replace('</h2>','').strip()
            # date =div.xpath('./div[1]')[0].extract().replace('<div class="xxl-date">','').replace('</div>','')
            # content = div.xpath('./div[2]')[0].extract().replace('<div class="xxl-des">','').replace('</div>','')

            # important:解析方案2,这样就不用加上[0]来提取列表中的第一个元素了
            title = div.xpath('./h2').extract_first().replace('<h2>', '').replace('</h2>', '').strip()
            date = div.xpath('./div[1]').extract_first().replace('<div class="xxl-date">', '').replace('</div>', '')
            content = div.xpath('./div[2]').extract_first().replace('<div class="xxl-des">', '').replace('</div>', '')

            # print(title)
            # print(type(title))
            # runtime_result:
            '''
            <h2>你叫“一点不紧张女士”吗？</h2>
            <class 'scrapy.selector.unified.Selector'> 返回的不是我们想要的字符串而是一个Selector对象
            '''


            # important:调用.extract()
            # print(title.extract())
            # print(type(title.extract()))
            # runtime_result:
            '''
            <h2>你叫“一点不紧张女士”吗？</h2>
            <class 'str'> <--这样就是字符串形式了
            '''
            print(title)
            print(date)
            print(content)
            # important:scrapy爬取速度是非常快的因为它本身是异步的
            break