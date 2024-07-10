# @Editor    : 百年
# @FileName  :08易车网车评获取.py
# @Time      :2024/7/8 16:42
from pyquery import PyQuery
import requests
import random
import csv

# 输入要获取的车评价的车名拼音
at_name = input("请输入车名拼音,如果不知到请先到易车网搜索https://dianping.yiche.com:")
# fp = open(f'../others/{at_name}车评.csv', 'a+', encoding='utf-8', newline='')
# 如果你对绝对路径或相对路径的知识不了解就这样写
fp = open(f'./{at_name}车评.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
# 接入第三方代理
proxies_pool = [
    {'http': '114.231.46.176:8089'},
    {'http': '117.69.237.179:8089'},
    {'http': '183.164.243.162:8089'},
    {'http': '111.224.212.41:8089'},
    {'http': '117.69.236.18:8089'},
    {'http': '121.41.98.141:80'},
    {'http': '113.124.84.192:9999'},
    {'http': '36.6.144.115:8089'},
    {'http': '123.182.59.163:8089'},
    {'http': '36.6.145.41:8089'},
    {'http': '101.34.77.44:80'},
    {'http': '27.214.50.121:9000'},
    {'http': '60.174.1.210:8089'},
    {'http': '114.231.42.89:8888'},
    {'http': '117.57.92.132:8089'},
    {'http': '36.6.145.178:8089'},
    {'http': '121.43.232.142:80'},
    {'http': '123.182.58.84:8089'},
    {'http': '116.62.35.202:80'},
    {'http': '113.223.213.242:8089'},
    {'http': '117.71.132.139:8089'},
    {'http': '114.232.110.64:8089'},
    {'http': '60.188.5.212:80'},
    {'http': '203.74.125.18:8888'},
    {'http': '121.41.57.227:80'},
    {'http': '123.182.59.184:8089'},
    {'http': '117.69.236.26:8089'},
    {'http': '117.71.149.133:8089'},
    {'http': '114.231.82.82:8888'},
    {'http': '36.6.145.203:8089'},
    {'http': '117.70.49.102:8089'},
    {'http': '36.6.145.166:8089'},
    {'http': '114.231.82.131:8089'},
    {'http': '183.164.243.71:8089'},
    {'http': '114.231.82.87:8089'},
    {'http': '60.174.0.154:8089'},
    {'http': '60.174.0.197:8089'},
    {'http': '111.225.152.176:8089'},
    {'http': '111.225.153.243:8089'},
    {'http': '36.6.145.178:8089'},
    {'http': '121.43.232.142:80'},
    {'http': '123.182.58.84:8089'},
    {'http': '116.62.35.202:80'},
    {'http': '113.223.213.242:8089'},
    {'http': '117.71.132.139:8089'},
    {'http': '114.232.110.64:8089'},
    {'http': '60.188.5.212:80'},
    {'http': '203.74.125.18:8888'},
    {'http': '121.41.57.227:80'},
    {'http': '123.182.59.184:8089'},
    {'http': '117.69.236.26:8089'},
    {'http': '117.71.149.133:8089'},
    {'http': '114.231.82.82:8888'},
    {'http': '36.6.145.203:8089'},
    {'http': '117.70.49.102:8089'},
    {'http': '36.6.145.166:8089'},
    {'http': '114.231.82.131:8089'},
    {'http': '183.164.243.71:8089'},
    {'http': '114.231.82.87:8089'},
    {'http': '60.174.0.154:8089'},
    {'http': '60.174.0.197:8089'},
    {'http': '111.225.152.176:8089'},
    {'http': '111.225.153.243:8089'},
    {'http': '114.231.8.41:8888'},
    {'http': '114.232.109.72:8089'},
    {'http': '183.164.243.181:8089'},
    {'http': '117.71.155.214:8089'},
    {'http': '114.116.252.222:443'},
    {'http': '36.6.145.244:8089'},
    {'http': '120.27.147.43:80'},
    {'http': '117.69.236.184:8089'},
    {'http': '183.165.251.209:8089'},
    {'http': '120.55.75.94:80'},
    {'http': '180.119.94.181:8089'},
    {'http': '113.223.213.118:8089'},
    {'http': '27.147.24.205:8080'},
    {'http': '113.223.213.77:8089'},
    {'http': '110.242.49.227:8080'}
]

proxies = random.choice(proxies_pool)

base_url = f'https://dianping.yiche.com/{at_name}/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
startpage = int(input('请输入要获取到起始页数>>'))
endpage = int(input('请输入终止页数>>'))
for i in range(startpage, endpage):
    new_url = base_url + f"koubei-{i + 1}.html"
    response = requests.get(url=new_url, headers=headers, proxies=proxies)
    response.encoding = response.apparent_encoding
    content = response.text
    # print(content)
    source = PyQuery(content)
    targetblock = source(".cm-content-box .cm-content-moudle").items()
    for item in targetblock:
        # print(item)
        # 1用户名
        username = item('.cm-user-name').text()
        # print(username)
        # 2评论日期
        comm_date = item('.cm-user-panel p span').text()
        # print(comm_date)
        # 3车型
        car_type = item('.cm-car-name').text()
        # print(car_type)
        # 4评分
        score = item('.score').text()
        # print(score)
        # 5裸车价
        car_price = item('.cm-car-price-value').text()
        # print(car_price)
        # 6油耗
        oil = item('.cm-car-oil-value').text()
        # print(oil)

        # 7购车时间
        buy_time = item('.cm-car-buy-time-value').text()
        # print(buy_time)
        # 8 评价内容
        comment = item('.cm-content p').text()
        # print(comment)
        # print(username, comm_date, car_type, score, car_price, oil, buy_time, comment)
        info_all = [username, comm_date, car_type, score, car_price, oil, buy_time, comment]
        writer.writerow(info_all)
        print(info_all)
print('程序结束')
fp.close()
