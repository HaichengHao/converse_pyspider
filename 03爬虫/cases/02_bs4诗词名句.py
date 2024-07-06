# @Editor    : 百年
# @FileName  :10诗词名句.py
# @Time      :2024/7/1 8:29
from bs4 import BeautifulSoup
import requests
import random
fp=open('../others/10诗词名句.txt', 'a+',encoding='utf-8')
# proxies_pool = [
#     {'http': '39.173.106.249:80'},
#     {'http':'39.105.27.30'},
#     {'http':'125.77.25.178'}
#
# ]
# proxies = random.choice(proxies_pool)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}
url='https://www.shicimingjv.com/songci/index_1.html'
response=requests.get(url=url,headers=headers)
response.encoding = response.apparent_encoding
content=response.text
# print(content)
page_html=BeautifulSoup(content,'lxml')
titles=page_html.find_all('h3',attrs={'class': 'item-title'})
# print(titles)
dy_=page_html.find_all('span',attrs={'class': 'chaodai'})
# print(dy_)
author=page_html.find_all('a',attrs={'class': 'nickname'})
# print(author)
item_expert=page_html.find_all('div',attrs={'class': 'item-excerpt'})
print(item_expert)
# 关于zip查看python基础37
for item in zip(titles,dy_,author,item_expert):
    poem_title=item[0].text
    poem_dynasty=item[1].text
    poem_author=item[2].text
    poem_content=item[3].text.strip()
    fp.write(f'题目:\t{poem_title}\n 朝代:{poem_dynasty},{poem_author}\n{poem_content}\n')
    print('-------')
fp.close()
#     print(a.text)
# def get_content(url, headers):
#     response = requests.get(url, headers)
#     response.encoding = response.apparent_encoding
#     content = response.text
#     return content
#
#
# def parsecontent(content):
#     page = BeautifulSoup(content, 'html.parser')
#
#
# if __name__ == '__main__':
#     page_source = get_content(url='https://www.shicimingjv.com/songci/index_1.html', headers=headers)
#     print(page_source)
