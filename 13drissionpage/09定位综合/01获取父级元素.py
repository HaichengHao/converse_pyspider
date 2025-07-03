# @Author    : 百年
# @FileName  :01获取父级元素.py
# @DateTime  :2025/7/3 11:52
from DrissionPage import WebPage

url = 'https://mil.news.sina.com.cn/'
page = WebPage()
page.get(url)
print(page.html)

