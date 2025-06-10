"""
@File    :runspider.py
@Editor  : 百年
@Date    :2025/6/9 15:07 
"""
from scrapy.cmdline import execute
if __name__ == '__main__':
    execute("scrapy crawl demo".split())