# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


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

    def process_item(self, item, spider):
        # SQL 插入语句
        sql = "INSERT INTO caipiao (date, red_ball, blue_ball) VALUES (%s, %s, %s)"

        # 执行SQL语句，并传入参数
        try:
            self.cursor.execute(sql, (item['date'].strip(), item['red_ball'], item['blue_ball']))
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

        return item


    def close_spider(self, spider):
        self.conn.close()  # tips:将数据库链接关闭

class CaipiaoPipeline:
    def open_spider(self,spider):
        self.fp = open('./双色球,csv', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        item['red_ball'] = ','.join(item['red_ball']) if item['red_ball'] else None
        item['blue_ball'] = ','.join(item['blue_ball']) if item['blue_ball'] else None
        self.fp.write(f"{item['date'].strip()},{item['red_ball']},{item['blue_ball']}\n")
        print(item)
        return item
    def close_spider(self, spider):
        self.fp.close()
