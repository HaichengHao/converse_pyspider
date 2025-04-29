import scrapy
from scrapy_splash.request import SplashRequest
from scrapy_redis.spiders import RedisSpider
from ..items import NewsItem


class WangyiSpider(RedisSpider):
    name = "news"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/domestic/"]
    # redis_key = 'wangyi:news:start_urls' #tips:因为要实现分布式，所以要上redis_key,但是又因为我们已经重写了start_requests，现在支持scrapy_redis,所以不需要再写
    lua_source = """
    function main(splash, args)
      assert(splash:go(args.url))
      assert(splash:wait(0.5))

      get_btn_display = splash:jsfunc([[
        function(){
        return document.getElementsByClassName('load_more_btn')[0].style.display;
      }
        ]])
      while(true)
      do
      splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
      splash:select(".load_more_btn").click()
      splash:wait(1)
      -- 判断load_more_btn是否为none
      display = get_btn_display()
      if(display == 'none')
      then 
          break
      end
     end
     assert(splash:wait(2))
    return {
        html = splash:html(),
    }
    end

    """

    # important:重写父类
    def start_requests(self):  # tips:这里的思路和06 scrapy boss里的处理selenium的思路很相似
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint="execute",  # important:表示要执行哪一个splash的服务
            args={
                "lua_source": self.lua_source,
            },
            # cookies={} 也可以传入已经切割为字典形式的cookies
            dont_filter=True #tips:因为只是爬这一页的数据，所以不需要去重，那么布隆过滤器即使生效也不会在redis里有request和bloomfilter
        )

    def parse(self, response):
        # print(response.text)
        # 注意这里和之前的有所不同,scrapy_splash返回的不再是json格式的响应信息，所以这里我们可以不再进行json数据格式与python格式的转换
        # json_response = response.json()
        # responseraw = json_response['html']
        # print(responseraw)
        # response = HtmlResponse(url=self.start_urls[0],body=responseraw,encoding='utf-8')
        # titles = response.xpath('//div[contains(@class, "news_title")]//a/text()').extract()
        # hrefs = response.xpath('//div[contains(@class, "news_title")]//a/@href').extract()
        # for title in titles:
        #     print(title)
        a_s = response.xpath('//div[contains(@class, "news_title")]//a')
        for a in a_s:
            title = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            item = NewsItem()
            item['title'] = title
            item['href'] = href
            print(f'Title: {title}, Href: {href}')
            yield item
