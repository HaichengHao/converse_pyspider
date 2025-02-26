import scrapy


class GamedataSpider(scrapy.Spider):
    name = "gamedata"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.4399.com/"]

    def parse(self, response):
        li_s = response.xpath('//*[@id="skinbody"]/div[10]/div[1]/div[1]/ul/li')

        for li in li_s:
            game_name = li.xpath('./a/text()').extract_first()
            game_url = li.xpath('./a/@href').extract_first()
            print(game_name,game_url)

