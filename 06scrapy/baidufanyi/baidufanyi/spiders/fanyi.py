import scrapy


# important:学习本节可以先回顾一下04_requests的post请求
class FanyiSpider(scrapy.Spider):
    name = "fanyi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://fanyi.baidu.com/sug"]
    #important:重写start_requests方法
    def start_requests(self):  # tips:父类（scrapy.Spider）中的方法，该方法是用来给起始的url列表中的每一个url发请求的
        data = {
            'kw': input('请输入你要翻译的汉字>>>')
        }
        for url in self.start_urls:
            # yield scrapy.Request(url=url,callback=self.parse) #tips:这个是发送之前学的GET请求,当然它可以加上method='POST'但是不建议
            # important:我们常用scrapy.FormRequest()来发送POST请求
            yield scrapy.FormRequest(url=url, callback=self.parse,
                                     formdata=data)  # important:formdata是用来指定请求参数的，对比requests的post请求来学习

    def parse(self, response):
        res = response.json()['data'][0]['v'] #important:返回的是json格式的数据
        print(res)
#         tips:如果想在详情页面中发送post请求那就像下面的写法
'''
     def parse(self, response):
        detail_url = response.xpath('...')
        yield scrapy.FormRequest(url=detail_url)
            
'''

#summary:对起始的url发送post请求一定要重写父类方法start_request,
#  生成请求改写为scrapy.FormRequest()
# 如果没明白可以先看看scrapy.Spider的__init__.py文件中的start_requests方法是怎么写的
