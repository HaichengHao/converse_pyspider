# @Editor    : 百年
# @FileName  :06利用re爬取豆瓣top250.py
# @Time      :2024/4/29 9:19
import random
import re
import requests
import csv  # 关于csv文件的读写操作，查看02python高阶/17python文件读写之CSV

fp = open('../others/doubantop250new.csv', 'a+', encoding='utf-8',
          newline='')  # 其中newline=""表示不再进行换行，因为csv.write()会默认换行，所以如果不加这个会出现隔行问题
writer = csv.writer(fp)
url = "https://movie.douban.com/top250?start="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
# proxies = [
#     {'http': '42.63.65.37:80'},
#     {'http': '42.63.65.13:80'},
#     {'http': '42.63.65.15:80'},
#     {'http': '42.63.65.7:80'},
#     {'http': '42.63.65.8:80'},
#     {'http': '42.63.65.9:80'},
#     {'http': '39.173.106.248:80'},
#     {'http': '39.173.106.249:80'},
# ]
#
# proxy = random.choice(proxies)
for i in range(0, 226, 25):
    new_url = url + str(i)
    response = requests.get(url=new_url, headers=headers)
    content = response.text
    # print(content)

    # 查看是否爬取到了
    # print(content)
    # 接下来我们利用re来定制我们要爬取到的数据
    # 1预加载
    moviestitle = re.compile(
        r'<div class="item">.*?<span class="title">(?P<moviename>.*?)</span>.*?<p class="">.*?导演:(?P<editor>.*?)&nbsp;.*?主演:(?P<actor>.*?)<br>.*?(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<numbersofevaluators>.*?)</span>',
        re.S)  # re.S可以让正则中的.匹配换行符
    # 2调用re模块的方法，注意要将待匹配内容其转化为字符串类型先看看匹配到了什么，之后我们用迭代器
    result = moviestitle.finditer(content)
    print(result)
    # [] 空列表，这是为什么呢？因为最开始我们没有加上re.S，修改后再次运行查看结果
    # <callable_iterator object at 0x00000129CF79AFB0> <--加上之后成功，我们利用01Python基础回顾中的41提取分组数据中的提取方式来对迭代器内容进行提取
    for item in result:
        name = item.group("moviename")
        editor = item.group("editor")
        actor = item.group("actor")
        year = item.group("year").strip()  # 利用字符串中的方法.strip()将字符串的左右换行/空格等处理掉
        score = item.group("score")
        numbersofevaluators = item.group("numbersofevaluators")
        print(name, editor, actor, year, score, numbersofevaluators)
        movieinfo = [name, editor, actor, year, score, numbersofevaluators]
        writer.writerow(movieinfo)

fp.close()
response.close()
