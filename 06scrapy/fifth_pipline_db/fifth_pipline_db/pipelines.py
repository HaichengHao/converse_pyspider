# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#important:爬虫文件会将item提交给优先级最高的管道类，优先级最高的管道类的
# process_item中要写return item操作，该操作就是表示将item对象传递给下一个管道类，
#  下一个管道类获取了item对象才可以将数据保存成功

# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
import redis
# 既然想用mysql的pipline那就需要导入pymysql或者mysqlconnector
import mysql.connector
import csv
# important:负责将数据存储到mysql中
class MySqlPipeline: #important:这里修改了名称的话需要到piplines.py中把管道配置成相同名称
    conn = None
    cursor = None
    # important:和文件管道一样，只需要开启一次链接，关闭一次链接而非多次开启和关闭数据库链接
    #  所以还是利用open_spider和close_spider只会在spider(就是写的主爬虫文件)文件前后运行一次的特性
    def open_spider(self,spider):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='spider',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        title = item['title']
        sql = 'insert into xiaoshuo(title) values ("%s")'%title
        self.cursor.execute(sql)
        self.conn.commit() #important:操作完毕后将操作提交
        print('成功写入一条数据')
        return item
    def close_spider(self,spider):
        self.conn.close() #tips:将数据库链接关闭

# 将数据存储到redis中 ,注意去setting的管道里头添加管道
class RedisPipeline:
    conn = None
    def open_spider(self,spider):
        # important:在连接前记得启动服务
        # tips:redis-server.exe
        # tips:然后换一个窗口 redis-cli.exe
        self.conn=redis.Redis(host='127.0.0.1',port=6379)
        print(self.conn)
    def process_item(self,item,spider):
        # title = item['title']
        # important:如果想将一个python字典直接写入到Redis中则redis版本必须是2.10.6
        self.conn.lpush('xiaoshuo',item) #tips:将item存在我们起名的叫xiaoshuo的列表中
        print('数据存储redis成功')
        return item
        #important:如果不是则重新安装pip install redis==2.10.6
        #tips:如果不想降级，那就照着下面的写法
        # title = item['title']
        # self.conn.lpush('xiaoshuo',title)
    # def close_spider(self,spider):
    #     self.conn.close() #其实redis一般不用代码来关闭服务，而是只需要在redis的cmd窗口ctrl+c关闭就可以了
# important:负责将数据存储到文件中
class FifthPiplineDbPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp = open('demo.txt','w',encoding='utf-8')
        print('写入文件创建成功')
    def process_item(self, item, spider):
        # important:爬虫文件每向管道提交一个item,则process_item方法就会被调用一次
        # tips:取数据
        title = item['title']
        self.fp.write(title+'\n')
        print(f'{title}写入成功')
        return item
    def close_spider(self,spider):
        self.fp.close()
        print('文件写入成功,正常关闭')
# important:将数据写入csv当中
class toCsv:
    fp = None
    def open_spider(self,spider):
        self.fp = open('Data.csv','a+',encoding='utf-8',newline='')
        self.writer = csv.writer(self.fp)
        # 判读表头是否为空，如果为空就写入表头
        if self.fp.tell() == 0:
            self.writer.writerow(['标题'])
        print('csv文件创建成功')
    def process_item(self,item,spider):
        title = item['title']
        self.writer.writerow([title,])
        return item
    def close_spider(self,spider):
        self.fp.close()


# 存储到mongodb当中，这部分需要看caipiao的，那个写的比较详细
class MongoPipline:

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(
            host='127.0.0.1',
            port=27017
        )
        db = self.client['spider'] #step 指定要使用的数据库
        # db.authenticate('admin', 'admin123')
        self.collection = db['c1'] #step 指定使用的集合
    def process_item(self,items,spider):
        # step 向集合中插入数据
        self.collection.insert({
            "title": items['title'],
        })
    def close_spider(self, spider):
        self.client.close()