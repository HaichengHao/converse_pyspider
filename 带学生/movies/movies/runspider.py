"""
@File    :runspider.py
@Editor  : 百年
@Date    :2025/5/29 22:12 
"""

from scrapy.cmdline import execute

if __name__ == '__main__':
    execute("scrapy crawl movie".split())
