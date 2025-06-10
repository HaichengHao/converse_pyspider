# @Editor    : 百年
# @FileName  :08豆瓣书评xpath_单.py
# @Time      :2024/8/23 16:07
from lxml import etree
import requests
import random
import sqlite3

filepath = './douban.txt'
proxies_pool = [
    {'http': '114.231.45.224:8888'},
    {'http': '114.103.88.253:8089'},
    {'http': '223.215.177.237:8089'},
    {'http': '114.231.41.56:8089'},
    {'http': '118.31.1.128:80'},
    {'http': '121.41.99.161:80'},
    {'http': '117.71.149.168:8089'},
    {'http': '112.243.228.40:9000'},
    {'http': '182.34.20.6:9999'},
    {'http': '183.164.242.35:8089'},
    {'http': '42.63.65.104:80'},
    {'http': '183.166.170.138:41122'},
    {'http': '114.231.8.26:8888'},
    {'http': '47.96.38.188:80'},
    {'http': '113.223.215.142:8089'},
    {'http': '123.182.58.95:8089'},
    {'http': '123.182.58.217:8089'},
    {'http': '114.55.109.154:80'},
    {'http': '114.232.110.136:8089'},
    {'http': '114.231.8.15:8089'},
    {'http': '113.121.40.189:9999'},
    {'http': '117.71.149.67:8089'},
    {'http': '60.174.1.54:8089'},
    {'http': '121.40.160.211:80'},
    {'http': '111.225.153.246:8089'},
    {'http': '111.225.153.150:8089'},
    {'http': '49.71.144.83:8089'},
    {'http': '101.37.163.83:80'},
    {'http': '111.225.152.48:8089'},
    {'http': '117.71.132.26:8089'},
    {'http': '182.34.26.109:9999'},
    {'http': '61.160.202.73:80'},
    {'http': '60.5.254.16:8080'},
    {'http': '39.173.106.239:80'},
    {'http': '210.13.117.18:443'},
    {'http': '114.231.45.3:8888'},
    {'http': '42.63.65.73:80'},
    {'http': '117.57.92.207:8089'},
    {'http': '114.231.46.104:8089'},
    {'http': '123.182.58.95:8089'},
    {'http': '123.182.58.217:8089'},
    {'http': '114.55.109.154:80'},
    {'http': '114.232.110.136:8089'},
    {'http': '114.231.8.15:8089'},
    {'http': '113.121.40.189:9999'},
    {'http': '117.71.149.67:8089'},
    {'http': '60.174.1.54:8089'},
    {'http': '121.40.160.211:80'},
    {'http': '111.225.153.246:8089'},
    {'http': '111.225.153.150:8089'},
    {'http': '49.71.144.83:8089'},
    {'http': '101.37.163.83:80'},
    {'http': '111.225.152.48:8089'},
    {'http': '117.71.132.26:8089'},
    {'http': '182.34.26.109:9999'},
    {'http': '61.160.202.73:80'},
    {'http': '60.5.254.16:8080'},
    {'http': '39.173.106.239:80'},
    {'http': '210.13.117.18:443'},
    {'http': '114.231.45.3:8888'},
    {'http': '42.63.65.73:80'},
    {'http': '117.57.92.207:8089'},
    {'http': '114.231.46.104:8089'},
    {'http': '120.26.14.131:80'},
    {'http': '117.71.154.175:8089'},
    {'http': '120.27.143.33:80'},
    {'http': '223.215.176.10:8089'},
    {'http': '111.225.153.238:8089'},
    {'http': '114.106.172.37:8089'},
    {'http': '118.31.247.119:80'},
    {'http': '117.71.149.113:8089'},
    {'http': '42.63.65.15:80'},
    {'http': '183.165.245.254:8089'},
    {'http': '61.135.169.121:80'},
    {'http': '36.6.145.49:8089'},
    {'http': '221.122.91.64:80'},
    {'http': '111.225.153.81:8089'},
    {'http': '36.6.144.6:8089'}

]
proxies = random.choice(proxies_pool)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}


def get_content(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    # response.encoding = response.apparent_encoding
    content = response.text
    return content


def parse_content(content):
    tree = etree.HTML(content)
    comments = tree.xpath('//p[@class="comment-content"]/span/text()')
    return comments


def down_load(page, comments):
    with open('./douban2.txt', 'a+', encoding='utf-8') as file:
        for item in comments:
            file.write(str(item))
            file.write('\n')
    print('第' + str(page) + '页爬取结束')


def save2db(comments, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS comments(id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)")
    for item in comments:
        cursor.execute("INSERT INTO comments(comm) VALUES (?)", (item,))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    startpage = int(input('请输入起始页>>'))
    endpage = int(input('请输入终止页>>'))
    book_id = input("请输入书籍号>>")
    for i in range(startpage, endpage + 1):
        url = f'https://book.douban.com/subject/{book_id}/comments/?start={(i - 1) * 20}&limit=20&status=P&sort=score'
        content = get_content(url)
        comment = parse_content(content)
        down_load(i, comment)
        # save2db(comment, 'douban.db')
    print("运行结束")
