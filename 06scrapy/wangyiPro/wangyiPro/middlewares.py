# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy.http import HtmlResponse #导入这个模块方便我们处理动态加载的页面数据


# important:scrapy 封装的响应对象对应的类，通过这个类可以创建一个响应对象

class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):
        # important:要处理的只有需要动态加载的四个板块的url的响应对象，其余的请求(如第一个主页请求)并非动态加载
        #   现在最重要的就是如何筛选出指定的4个板块对应的响应对象
        # tips:可以先找出指定4个板块的请求对象，根据请求对象定位到响应对象
        #   可以根据4个板块的url定位到4个响应对象
        # 让middlewares.py与主爬虫文件.py进行数据交互
        model_urls = spider.model_urls
        # tips: 拿到每个请求对象的url
        if request.url in model_urls:  # important:进行判断，如果请求的url在model_urls当中就发起请求
            browser =  spider.browser #tips:从爬虫类中获取创建好的浏览器对象
            browser.get(request.url) #对拦截到的请求对象发起请求
            time.sleep(4)
            page_text = browser.page_source #返回selenium加载出的页面数据，然后将这个数据给body
            response = HtmlResponse(url=request.url, request=request, encoding='utf-8', body=page_text)  # important:body就是响应对象的响应数据
            return response
        else:  # tips: 如果不是那几个需要动态加载的url，就不做处理，直接将其返回
            return response

    def process_exception(self, request, exception, spider):

        pass
