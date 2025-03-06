# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
import mysql.connector
# from settings import MY_SQL #另一种方式导入数据库

# important:负责将数据存储到mysql中
class MySqlPipeline:  # important:这里修改了名称的话需要到piplines.py中把管道配置成相同名称
    conn = None
    cursor = None

    # important:和文件管道一样，只需要开启一次链接，关闭一次链接而非多次开启和关闭数据库链接
    #  所以还是利用open_spider和close_spider只会在spider(就是写的主爬虫文件)文件前后运行一次的特性
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='caipiao',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        # tips:新的写法
        # self.conn = mysql.connector.connect(
        #     host=MY_SQL['host'],
        #     port=MY_SQL['port'],
        #     user=MY_SQL['user'],
        #     password=MY_SQL['password'],
        #     database=MY_SQL['database'],
        #     charset=MY_SQL['charset']
        # )
        # self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # SQL 插入语句
        sql = "INSERT INTO caipiao (date, red_ball, blue_ball) VALUES (%s, %s, %s)"

        # important:执行SQL语句，并传入参数,注意，是个元组
        try:
            self.cursor.execute(sql, (item['date'].strip(), item['red_ball'], item['blue_ball']))
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback() #tips:如果出错了就回滚
        return item


    def close_spider(self, spider):
        self.conn.close()  # tips:将数据库链接关闭


# 存储为csv文件
class CaipiaoPipeline:
    def open_spider(self,spider):
        self.fp = open('./双色球.csv', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        item['red_ball'] = ','.join(item['red_ball']) if item['red_ball'] else None
        item['blue_ball'] = ','.join(item['blue_ball']) if item['blue_ball'] else None
        self.fp.write(f"{item['date'].strip()},{item['red_ball']},{item['blue_ball']}\n")
        print(item)
        return item
    def close_spider(self, spider):
        self.fp.close()


# 存储到mongodb当中
class MongoPipeline:

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(
            host='127.0.0.1',
            port=27017
        )
        db = self.client['spider'] #step 指定要使用的数据库
        # db.authenticate('admin', 'admin123')
        self.collection = db['caipiao'] #step 指定使用的集合
    def process_item(self,item,spider):
        # step 向集合中插入数据
        self.collection.insert_one({
            "qihao": item['date'],
            "red_ball": item['red_ball'],
            "blue_ball":item['blue_ball']
        })
    def close_spider(self, spider):
        self.client.close()


