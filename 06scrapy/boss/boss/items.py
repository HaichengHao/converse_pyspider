# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    job_name = scrapy.Field()
    job_area = scrapy.Field()
    salary = scrapy.Field()