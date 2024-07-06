# @Editor    : 百年
# @FileName  :03本草纲目.py
# @Time      :2024/7/2 10:26
from  bs4 import BeautifulSoup
import  requests
import random
url='https://www.shicimingjv.com/bookindex/24.html'
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
    # print(f'章节名:{title},链接:{link}')
    # 访问详情页面并得到文章内容并将每一章都保存为一个新的文件
    new_response=requests.get(url=link,headers=headers)
    new_content = new_response.text
    # print(new_content)
    new_page_source = BeautifulSoup(new_content, 'lxml')
    entry_content = new_page_source.select('div.entry-content >p:nth-child(-n+4)')
    # print(entry_content)
    try:
        othername = entry_content[1].text
    except IndexError:
        othername = ''
    try:
        taste = entry_content[2].text
    except IndexError:
        taste = ''
    try:
        power = entry_content[3].text
    except IndexError:
        power=''
    print(f'{othername}\n{taste}\n{power}')