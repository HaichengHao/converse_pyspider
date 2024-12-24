#ABST:本节主要讲的是将获取到的信息利用持久化存储(本节用的是终端指令持久化存储的方式，下节将会使用管道)
# important:只可以将parse方的返回值存储到指定后缀(csv)的文本文件中(其局限性很大，所以简单理解，重点放在管道)
import scrapy


class DuanziSpider(scrapy.Spider):
    name = "savedatademo"
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
        # 创建一个列表用于整合数据
        all_data=[]
        for div in divlst:
            # important:解析方案2,这样就不用加上[0]来提取列表中的第一个元素了
            title = div.xpath('./h2').extract_first().replace('<h2>', '').replace('</h2>', '').strip()
            date = div.xpath('./div[1]').extract_first().replace('<div class="xxl-date">', '').replace('</div>', '')
            content = div.xpath('./div[2]').extract_first().replace('<div class="xxl-des">', '').replace('</div>', '')
            # tips:因为指令持久化存储需要parse给返回值
            dic={'title':title,'date':date,'cotent':content}
            all_data.append(dic) #将数据添加到列表当中
            # important:scrapy爬取速度是非常快的因为它本身是异步的
            # break
        return all_data #将所有数据返回
    # important:在终端输入下面的命令，将其保存到csv文件当中去
    # tips: scrapy crawl savedatademo -o duanzi.csv
    # summary:
    #  优点: 简单便捷
    #  缺点：局限性强
    #     1只可以将存储数据存储到文本文件而无法写入到数据库
    #     2存储数据文件后缀是指定好的，通常使用.csv
    #     3需要将存储的数据封装到parse方法的返回值当中