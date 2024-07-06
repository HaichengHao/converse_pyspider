# @Editor    : 百年
# @FileName  :07电影天堂网.py
# @Time      :2024/4/29 17:48
# 电影天堂最近更新

import random
import re
import requests
import csv

fp = open('../others/dytt.csv', 'w+', encoding='utf-8', newline='')
writer = csv.writer(fp)
# 首页url
baseurl = "https://www.btwuji.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.57",
    # "Cookie": "__51vcke__K84SQSvemveIs5ZA=c982306e-3026-5360-ba5f-9218c670363f; __51vuft__K84SQSvemveIs5ZA=1708833005377; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218ddfe724618-032ce13e3d50bd-26001851-1327104-18ddfe7246216c%22%7D; __vtins__K84SQSvemveIs5ZA=%7B%22sid%22%3A%20%22e4ae47b4-92f1-58b2-99c3-367b7a83f906%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201714400252699%2C%20%22ct%22%3A%201714398452699%7D; __51uvsct__K84SQSvemveIs5ZA=6"
}
proxies = [
    {'http': '42.63.65.37:80'},
    {'http': '42.63.65.13:80'},
    {'http': '42.63.65.15:80'},
    {'http': '42.63.65.7:80'},
    {'http': '42.63.65.8:80'},
    {'http': '42.63.65.9:80'},
    {'http': '39.173.106.248:80'},
    {'http': '39.173.106.249:80'}
]
proxy = random.choice(proxies)
response = requests.get(url=baseurl, headers=headers, proxies=proxy)
response.encoding = "gb2312"
content = response.text
# 1预加载匹配规则
target = re.compile(r'<div class="bd3l">.*?<div class="co_content2">.*?<ul>(?P<content>.*?)</ul>', re.S)
# 2调用.search()匹配指定的内容content,注意search只返回一个match结果,为啥用search呢？因为这里的内容就只有一项而已，没必要用finditer去迭代了
result = target.search(content)
# print(result)
urls = result.group("content")
# print(urls)
# print(type(urls))
# 定义获取详情页内容的新规则

new_target = re.compile(r"<a href='(?P<detail_page>.*?)'>.*?</a><br/>", re.S)
# # #拿出迭代器对象
result = new_target.finditer(urls)
print(result)
for page_url in result:
    detailpage_url = 'https://www.btwuji.com' + page_url.group("detail_page")
    print(detailpage_url)
    # 接下来我们以others文件夹中的07电影天堂二级页面验证为访问详情页面的主要思路来对获取到的新url进行访问
    newresponse = requests.get(url=detailpage_url, headers=headers, proxies=proxy)
    newresponse.encoding = "gb2312"
    newcontent = newresponse.text
    # print(newcontent)
    info = re.compile(
        r'<div id="Zoom">.*?<span style="FONT-SIZE: 12px">.*?<br />◎片　　名　(?P<name>.*?)<br />◎年　　代　(?P<year>.*?)<br />◎产　　地　(?P<region>.*?)<br />◎类　　别　(?P<type>.*?)<br />◎语　　言　(?P<language>.*?)<br />◎字　　幕　(?P<subtitle>.*?)<br />◎上映日期　(?P<releasedate>.*?)<br />◎IMDb评分&nbsp;&nbsp;(?P<IMDbscore>.*?).*?<br />◎豆瓣评分　(?P<doubanscore>.*?).*?<br />◎片　　长　(?P<film_length>.*?)<br />◎导　　演　(?P<editor>.*?)<br />.*?</a>',
        #     r'<div id="Zoom">.*?<span style="FONT-SIZE: 12px"><td>.*?◎译　　名　(?P<trs_name>.*?)<br />◎片　　名　(?P<name>.*?)<br />◎年　　代　(?P<year>.*?)<br />◎产　　地　(?P<region>.*?)<br />◎类　　别　(?P<type>.*?)<br />◎语　　言　(?P<language>.*?)<br />◎字　　幕　(?P<subtitle>.*?)<br />◎上映日期　(?P<releasedate>.*?)<br />◎IMDb评分&nbsp;&nbsp;(?P<IMDbscore>.*?).*?<br />◎豆瓣评分　(?P<doubanscore>.*?).*?<br />◎片　　长　(?P<film_length>.*?)<br />◎导　　演　(?P<editor>.*?)<br />.*?</a>',
        re.S)
    result = info.search(newcontent)
    # try:
    #     trans_name = result.group("trs_name")
    # except AttributeError:
    #     continue
    try:
        name = result.group("name")
    except:
        name = ''
    try:
        year = result.group("year")
    except:
        year = ''
    try:
        region = result.group("region")
    except:
        region = ''

    try:
        movie_type = result.group("type")
    except:
        movie_type = ''
    try:
        language = result.group("language")
    except:
        language = ''
    try:
        subtitle = result.group("subtitle")
    except:
        subtitle = ''
    try:
        releasedate = result.group("releasedate")
    except:
        releasedate = ''
    try:
        IMDbscore = result.group("IMDbscore")
    except:
        IMDbscore = ''
    try:
        doubanscore = result.group("doubanscore")
    except:
        doubanscore = ''
    try:
        film_length = result.group("film_length")
    except:
        film_length = ''
    try:
        editor = result.group("editor")
    except:
        editor = ''

    film_info = [name, year, region, movie_type, language, subtitle, releasedate, IMDbscore, doubanscore, film_length,
                 editor]
    print(film_info)
    writer.writerow(film_info)

fp.close()
