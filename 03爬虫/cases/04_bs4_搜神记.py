# @Editor    : 百年
# @FileName  :04_bs4_搜神记.py
# @Time      :2024/7/2 15:43
from  bs4 import BeautifulSoup
import  requests
import random
url='https://www.shicimingjv.com/bookindex/42.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}
response=requests.get(url=url,headers=headers)
content=response.text

page_source=BeautifulSoup(content,'lxml')
all_li=page_source.select('dl > ul > li')
# 获取章节详情页面的链接
all_a=page_source.select('dl > ul > li >a')
# print(all_a)
for li in zip(all_li,all_a):
    title = li[0].text
    link = li[1]['href']
    print(f'章节名:{title},链接:{link}')
    # 将爬取的文章写入到文本文件当中
    fp = open('../others/搜神记/'+str(title)+'.txt','a+',encoding='utf-8')
    # 访问详情页面并得到文章内容并将每一章都保存为一个新的文件
    # link = 'https://www.shicimingjv.com/bookview/4216.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }
    new_response = requests.get(url=link, headers=headers)
    new_content = new_response.text
    # print(new_content)
    new_page_source = BeautifulSoup(new_content, 'lxml')
    entry_content = new_page_source.find('div', attrs={'class': 'entry-content'})
    fp.write(entry_content.text)
    fp.close()
    # print(entry_content.text)