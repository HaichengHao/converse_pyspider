import scrapy


class FirstSpider(scrapy.Spider):
    name = "first" #tips:爬虫文件唯一标识 可以使用该变量的值来定位到唯一的一个爬虫文件，无需改动
    # important:allowed_domains一般不使用，将其注释掉
    # allowed_domains = ["www.xxx.com"] #tips:允许域名：scrapy只可以发起指定域名的网络请求
                                        # 例如我们指定的是www.xxx.com，那么在下方的起始url列表只有第一个https://www.xxx.com被允许发送网络请求
    start_urls = ["https://www.baidu.com/","https://www.bing.com"] #tips:起始的url列表，列表中存放的url可以被scrapy发起get请求

    # important:parse是用来做数据解析的
    # tips:参数Response:就是请求之后对应的响应对象
    #  parse的调用次数取决于start_urls列表元素的个数
    def parse(self, response):
        print('响应对象为:',response)
# tips:运行scrapy需要进到项目文件夹下打开终端输入scrapy crawl 爬虫文件唯一标识 [--nolog]
# runtime_result
'''
PS E:\converse_spider\converse_pyspider\06scrapy\firstdemo> scrapy crawl first --n
olog
响应对象为: <200 https://www.baidu.com/error.html>
响应对象为: <200 https://cn.bing.com/>
'''