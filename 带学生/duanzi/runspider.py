"""
@File    :runspider.py
@Editor  : 百年
@Date    :2025/5/28 14:05 
"""
from scrapy.cmdline import execute

if __name__ == '__main__':
    execute("scrapy crawl lezi".split())
