# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FourthPersistentStoragePiplinePipeline:
    # important:重写父类的方法
    fp = None #important:注意一定要先设定一个类变量fp，在类中的任何位置都可以使用，在类中它就是全局的
    def open_spider(self,spider):
        print('我是open_spider方法，我在项目开始运行环节只会被运行一次')
        self.fp = open('duanzi.txt','w',encoding='utf-8')
    # important：process_item用来接收爬虫文件传递过来的item对象
    # item参数就是管道接收到的item类型对象
    # process_item方法调用的次数取决于爬虫文件给其提交item的次数
    def process_item(self, item, spider):
        # print(item) #item类型的对象其实就是一个字典
        # runtime_result:
        '''
                {'content': '这句话（我自愿签订出门在外互帮父母条约），扎了多少年轻人的心，
        3月13日，山东威海，女生赶高铁看到腿脚不便独自出行的大叔，主动帮忙把行李搬上
        了阶梯。网友随后问道，下个路口怎么办？下个路口有千千万万个我   '
                    '...',
         'date': '2024年03月15日 10:58',
         'title': '我自愿签订出门在外互帮父母条约（年轻人扎心文案）'}
        '''
        # tips:下面的跟爬虫文件中的反着来就行
        title = item['title']
        date = item['date']
        content = item['content']
        self.fp.write(title+date+content+'\n')
        print(title,'标题的段子保存成功')
        return item
    #important:重写父类方法
    def close_spider(self,spider):
        print('在爬虫结束的时候会被执行一次')
        self.fp.close()