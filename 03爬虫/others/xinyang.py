# editor 百年
# date: 2023/12/27 16:01
'''
block_name //div[@class="tr-line"]/div[1]/div[2]
region //div[@class="tr-line"]/div[2]/div[2]/a[1]/text()
totalprice //div[@class="trl-item price_esf sty1"]/i/text()
house_type //div[@class="tr-line clearfix"][1]/div[@class="trl-item1 w146"][1]/div[1]
area //div[@class="tr-line clearfix"][1]/div[@class="trl-item1 w182"][1]/div[1]
unit_price //div[@class="tr-line clearfix"][1]/div[@class="trl-item1 w132"][1]/div[1]
orientation //div[@class="tr-line clearfix"][2]/div[@class="trl-item1 w146"][1]/div[1]
floor //div[@class="tr-line clearfix"][2]/div[@class="trl-item1 w182"][1]/div[1]
decoration //div[@class="tr-line clearfix"][2]/div[@class="trl-item1 w132"][1]/div[1]
elevator //div[@class="w1200 clearfix"]//div[@class="cont clearfix"]/div[1]/span[2]/text()
'''
import csv
import random
import sqlite3

import requests
from lxml import etree


# 定义爬取的请求头
def scrape_house_details(url, headers, proxies):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    response.encoding = 'GBK'
    content = response.text
    tree = etree.HTML(content)

    title = tree.xpath('//div[@class="content"]/div[@class="aroundInfo"]/div[@class="communityName"]/a[1]/text()')[0]
    totalprice = tree.xpath(
        '//div[@class="content"]/div[@class="price-container"]/div[@class="price "]/span[@class="total"]/text()')[
        0] if tree.xpath(
        '//div[@class="content"]/div[@class="price-container"]/div[@class="price "]/span[@class="total"]/text()') else ''
    folloer_numbers = tree.xpath('//div[@class="action"]/span[@id="favCount"]/text()')[0] if tree.xpath(
        '//div[@class="action"]/span[@id="favCount"]/text()') else ''
    unit_price = tree.xpath(
        '//div[@class="content"]/div[@class="price-container"]/div[@class="price "]/div[@class="text"]/div[@class="unitPrice"]/span/text()')[
        0] if tree.xpath(
        '//div[@class="content"]/div[@class="price-container"]/div[@class="price "]/div[@class="text"]/div[@class="unitPrice"]/span/text()') else ''
    region = tree.xpath(
        '//div[@class="content"]/div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]/a[1]/text()')[
        0] if tree.xpath(
        '//div[@class="content"]/div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]/a[1]/text()') else ''
    blockinfo = tree.xpath(
        '//div[@class="content"]/div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]/a[2]/text()')[
        0] if tree.xpath(
        '//div[@class="content"]/div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]/a[2]/text()') else ''
    house_type = tree.xpath('//div[@class="content"]/ul/li[1]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[1]/text()') else ''
    floor = tree.xpath('//div[@class="content"]/ul/li[2]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[2]/text()') else ''
    house_area = tree.xpath('//div[@class="content"]/ul/li[3]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[3]/text()') else ''
    house_type_area = tree.xpath('//div[@class="content"]/ul/li[4]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[4]/text()') else ''
    inside_area = tree.xpath('//div[@class="content"]/ul/li[5]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[5]/text()') else ''
    building_type = tree.xpath('//div[@class="content"]/ul/li[6]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[6]/text()') else ''
    orientation = tree.xpath('//div[@class="content"]/ul/li[7]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[7]/text()') else ''
    building_structer = tree.xpath('//div[@class="content"]/ul/li[8]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[8]/text()') else ''
    decoration = tree.xpath('//div[@class="content"]/ul/li[9]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[9]/text()') else ''
    user_elevator = tree.xpath('//div[@class="content"]/ul/li[10]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[10]/text()') else ''
    heating_method = tree.xpath('//div[@class="content"]/ul/li[11]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[11]/text()') else ''
    elevator = tree.xpath('//div[@class="content"]/ul/li[12]/text()')[0] if tree.xpath(
        '//div[@class="content"]/ul/li[12]/text()') else ''
    listing_time = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[1]/span[2]/text()')[
        0] if tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[1]/span[2]/text()') else ''
    transaction_ownership = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[2]/span[2]/text()')[
        0] if tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[2]/span[2]/text()') else ''
    last_transation_time = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[3]/span[2]/text()')[
        0] if tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[3]/span[2]/text()') else ''
    house_use = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[4]/span[2]/text()')[
        0] if tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[4]/span[2]/text()') else ''
    house_years = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[5]/span[2]/text()')[
        0] if tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[5]/span[2]/text()') else ''
    ownership = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[6]/span[2]/text()')[
        0] if tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[6]/span[2]/text()') else ''
    mortgage_info = tree.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[7]/span[2]/text()')[0].replace(
        '\n                                ', '').replace('\n                              ', '') if tree.xpath(
        '//div[@class="transaction"]/div[@class="content"]/ul/li[7]/span[2]/text()') else ''

    return [title, totalprice, unit_price, region, blockinfo, folloer_numbers, house_type, floor, house_area,
            house_type_area, inside_area, building_type, orientation, building_structer, decoration, user_elevator,
            elevator, listing_time, transaction_ownership, last_transation_time, house_use, house_years, ownership,
            mortgage_info]


# 定义函数，写入csv
# def write_to_csv(data, file_path):
#     with open(file_path, 'a+', encoding='utf-8', newline='') as fp:
#         writer = csv.writer(fp)
#         writer.writerow(data)

# 定义函数保存到数据库
def saveData2DB(data, dbpath):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO rentinfo (title, totalprice, unit_price, region, blockinfo, folloer_numbers, house_type, floor,
                              house_area, house_type_area, inside_area, building_type, orientation, building_structer,
                              decoration, user_elevator, elevator, listing_time, transaction_ownership,
                              last_transation_time, house_use, house_years, ownership, mortgage_info)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()


# 配置代理池和开始结束页面
def run_scraper(start_page, end_page):
    proxies_pool = [
        {'http': '183.221.242.103:9443'},
        {'http': '183.230.198.80:9091'},
        {'http': '183.221.242.103:9443'},
        {'http': '183.230.198.80:9091'},
        {'http': '183.172.197.188:4780'},
        {'http': '183.173.178.231:4780'},
        {'http': '183.172.169.225:4780'},
        {'http': '188.132.221.27:8080'},
        {'http': '103.152.232.134:8080'},
        {'http': '103.227.252.102:8080'},
        {'http': '79.106.170.34:8989'},
        {'http': '190.110.99.189:999'},
    ]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    # base_url = 'https://qd.lianjia.com/ershoufang/co32/pg'
    base_url = 'https://xinyang.esf.fang.com/house/i3'
    for i in range(start_page, end_page + 1):
        url = base_url + str(i) + '/'
        print(url)
        proxies = random.choice(proxies_pool)

        response = requests.get(url=url, headers=headers, proxies=proxies)
        content = response.text
        tree = etree.HTML(content)

        hrefs = tree.xpath('//dl/dd/h4/a/@href')
        print(hrefs)

        for j in range(len(hrefs)):
            new_url = 'https://xinyang.esf.fang.com' + str(hrefs[j])
            print(new_url)
            house_data = scrape_house_details(new_url, headers, proxies)
            # saveData2DB(house_data, "rentinfo.db")
            # print(house_data)


def init_db(dbpath):  # 创建数据表
    sql = '''
        CREATE TABLE IF NOT EXISTS rentinfo
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(50) NOT NULL,
        totalprice VARCHAR(50) NOT NULL,
        unit_price VARCHAR(50) NOT NULL,
        region VARCHAR(50) NOT NULL,
        blockinfo VARCHAR(50) NOT NULL,
        folloer_numbers VARCHAR(50) NOT NULL,
        house_type VARCHAR(50) NOT NULL,
        floor VARCHAR(50) NOT NULL,
        house_area VARCHAR(50) NOT NULL,
        house_type_area VARCHAR(50) NOT NULL,
        inside_area VARCHAR(50) NOT NULL,
        building_type VARCHAR(50) NOT NULL,
        orientation VARCHAR(50) NOT NULL,
        building_structer VARCHAR(50) NOT NULL,
        decoration VARCHAR(50) NOT NULL,
        user_elevator VARCHAR(50) NOT NULL,
        elevator VARCHAR(50) NOT NULL,
        listing_time VARCHAR(50) NOT NULL,
        transaction_ownership VARCHAR(50) NOT NULL,
        last_transation_time VARCHAR(50) NOT NULL,
        house_use VARCHAR(50) NOT NULL,
        house_years VARCHAR(50) NOT NULL,
        ownership VARCHAR(50) NOT NULL,
        mortgage_info VARCHAR(50) NOT NULL
        );
        '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # init_db("rentinfo.db")
    start_page_input = int(input("请输入起始页:"))
    end_page_input = int(input("请输入终止页:"))
    run_scraper(start_page_input, end_page_input)
