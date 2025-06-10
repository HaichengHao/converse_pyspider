"""
@File    :runningspider.py
@Editor  : 百年
@Date    :2025/6/6 9:19 
"""
from scrapy.cmdline import execute

if __name__ == '__main__':
    execute('scrapy crawl fanyi'.split())