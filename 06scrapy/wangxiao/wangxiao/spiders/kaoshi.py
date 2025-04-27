from urllib.parse import urljoin
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import scrapy
import json


class KaoshiSpider(scrapy.Spider):  # important:注意这里并没用到Ruel,所以不用换成CrawlSpider
    name = "kaoshi"
    # allowed_domains = ["www.xxx.cn"]
    start_urls = ["https://ks.wangxiao.cn/"]

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//div[@class="send-title"]/a')
        a_list = le.extract_links(response)
        for a in a_list:
            print(a.text, a.url)
            first_title = a.text  # important:一级目录标题
            exampoint_url = a.url.replace('TestPaper', 'exampoint')
            yield scrapy.Request(url=exampoint_url, callback=self.parse_second_level, meta={'first_title': first_title})
            break  # important:设置break是方便测试使用，这样只拿到第一个url就行，不然拿全部的出来进行爬虫会对目标服务器造成负担

    def parse_second_level(self, response):
        # important:接收上面请求传递的参数
        first_title = response.meta['first_title']

        # tips:还是用链接提取器
        le = LinkExtractor(restrict_xpaths='//div[@class="filter-item"][1]/a')
        a_list = le.extract_links(response)
        for a in a_list:
            second_title = a.text  # important:二级目录标题
            kemu_url = a.url
            # print(second_title,kemu_url)
            # tips:对第三层发起请求
            yield scrapy.Request(url=kemu_url, callback=self.parse_third_level,
                                 meta={'first_title': first_title, 'second_title': second_title})
            # break

    def parse_third_level(self, response):

        # important:接收其它函数携带的参数
        first_title = response.meta['first_title']
        second_title = response.meta['second_title']

        # print(response.text)
        # le = LinkExtractor(restrict_xpaths='')
        # important:这里要重新推一个思路，就是从里到外，先定位到最后一个节点，然后往外层直到最外层的节点
        # //ul[@class="section-item"]/li[3][position()]/span/@data_subsign #subsign定位

        points = response.xpath('//ul[@class="section-point-item"]')
        if points:  # 若非空则遍历
            for point in points:
                parents = point.xpath('./ancestor-or-self::ul[@class="chapter-item" or @class="section-item"]')
                # tips:xpath节点语法，意思是找到其长辈节点(不一定只有一个),可以指定为./ancestor-or-self::* 即为全都要，或者自己指定一个
                # tips:像上面这样意思就是找到ul[@class="chapter-item" or @class="section-item"]这个长辈就停止
                p_lst = [first_title, second_title]  # 创建长辈列表,将解析到的第一级和第二级名称放进去然后往里边插入数据
                # 拿到data-sign
                data_sign =point.xpath('./li[3]/span/@data_sign').extract_first()
                #important: 拿到data_sub_sign
                data_subsign = point.xpath('./li[3]/span/@data_subsign').extract_first()
                print(data_sign,data_subsign)
                for p in parents:
                    # tips:注意xpath解析的结果是一个列表,而我们想拿出列表中的字符串新增到新的列表p_lst进去,所以用到了.join操作,将解析出的含有span空字符串和text文本拼接然后进行了取出空格和换行符等
                    #   七四核写成p.xpath('./li[1]/text()').extract()[1].strip().replace(" ","") 也行
                    # fu_name = p.xpath('./li[1]/text()').extract()[1].strip().replace(" ", "")
                    fu_name = "".join(p.xpath('./li[1]/text()').extract()).strip().replace(" ","")  # tips:这里不能用extract_first()了，因为同级别<span>里有空文本
                    p_lst.append(fu_name)


                try:
                    # point_name = point.xpath('./li[1]/text()').extract()[0].strip().replace(" ", "")

                    point_name = "".join(point.xpath('./li[1]/text()').extract()).strip().replace(" ","")
                except IndexError:
                    point_name = ''
                print(p_lst,point_name)
                # runtime_result:
                """ 可以看看部分结果,这样我们就拿到了目录的树形结构列表
                ['第六章产业政策', '第一节产业政策概述']
                ['第六章产业政策', '第二节完善产业政策的部署与要求']
                ['第六章产业政策', '第三节我国的产业结构政策']
                ['第六章产业政策', '第四节我国的产业布局政策']
                ['第六章产业政策', '第五节医药、集成电路等产业的高质量发展政策']
                ['第七章社会政策', '第一节社会政策概述']
                ['第七章社会政策', '第二节我国的社会建设成就']
                ['第七章社会政策', '第三节新时代的社会建设目标与要求']
                ['第七章社会政策', '第四节当前社会建设的重点任务']
                ['第八章生态文明建设', '第一节习近平生态文明思想']
                ['第八章生态文明建设', '第二节推进经济绿色低碳循环发展']
                ['第八章生态文明建设', '第三节持续深入打好污染防治攻坚战']
                ['第八章生态文明建设', '第四节把碳达峰碳中和纳入生态文明建设整体布局']
                ['第八章生态文明建设', '第五节保护和修复重要生态系统']
                """
                data={
                    "practiceType":"2",
                    "sign":data_sign,
                    "subsign":data_subsign,
                    "examPointType":"",
                    "questionType":"",
                    "top":"100"}
                # important:注意这里看了request是payload的json传入的,并不是简单的data_dict,所以要将其序列化,不能用之前的FormRequest
                # yield scrapy.FormRequest(url='https://ks.wangxiao.cn/practice/listQuestions',callback=self.parse_timu,formdata=json.dumps(data))
                # formdata最终会吧data转变成key = value这样的形式
                yield scrapy.Request(
                    url='https://ks.wangxiao.cn/practice/listQuestions',
                    method='POST',
                    #important:这里利用请求体,传入的是json格式的data
                    body=json.dumps(data), #tips:这里是看到了request是payload类型,所以将其改成了json类型
                    headers={
                        'X-Requested-With':'XMLHttpRequest',
                        'content-type':'application/json; charset=UTF-8',
                        'origin':'https://ks.wangxiao.cn',
                        'referer':f'https://ks.wangxiao.cn/practice/getQuestion?practiceType=2&sign={data_sign}&subsign={data_subsign}&examPointType=&questionType=&top=100'
                    },
                    meta={
                        "p_lst":p_lst,
                        "point_name":point_name
                    },
                    callback=self.parse_timu, #向最终的解析函数发起调用
                )
        else:
            print('未能解析出数据,题目为空')

    def parse_timu(self,response):
        meta = response.meta
        p_lst = meta['p_lst']
        point_name = meta['point_name']
        print(response.text)


