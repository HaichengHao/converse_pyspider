# @Editor    : 百年
# @FileName  :搜神记新页面验证.py
# @Time      :2024/7/2 16:04
from bs4 import BeautifulSoup
import requests
link='https://www.shicimingjv.com/bookview/4216.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}
new_response=requests.get(url=link,headers=headers)
new_content=new_response.text
# print(new_content)
new_page_source=BeautifulSoup(new_content,'lxml')
entry_content=new_page_source.find('div',attrs={'class':'entry-content'})
print(entry_content.text)
# othername=entry_content[1].text
# taste=entry_content[2].text
# power=entry_content[3].text
# print(f'{othername}\n{taste}\n{power}')


