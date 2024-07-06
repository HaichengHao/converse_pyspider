# @Editor    : 百年
# @FileName  :08_bs4解析.py
# @Time      :2024/6/30 16:27
from bs4 import BeautifulSoup

html = '''
    <html>
        <body>
            <h1 id='title'> Beautiful Soup </h1>
            <p class='intro'>
                Beautiful Soup is a Python library for pulling data out of HTML and XML files.
            </p>
            <h1 id='title'> Beautiful Soup </h1>
            <ul class='lists'>
                <li id="tec">
                    <a href='http://www.w3.org/Protocols/r'>技术问题</a>
                </li>
                <li id="ntec">
                    <a href='http://www.baidu.com'>非技术问题</a>
                </li>
            </ul>
        </body>
    </html>
'''

# 1 初始化beautifulsoup对象
page = BeautifulSoup(html, "html.parser")
# a. page.find("标签名"[,attrs={"属性":"值"}]) #查找某个元素,且可以指定属性名和属性值，每次查找都只会返回一个结果，即第一个出现的匹配项目
# 例如，查找标签h1,且其id为title的元素
head1 = page.find("h1", attrs={"id": "title"})
# print(head1)
# <h1 id="title"> Beautiful Soup </h1>


# [<h1 id="title"> Beautiful Soup </h1>, <h1 id="title"> Beautiful Soup </h1>]

# 可以更深层次的查找,每个节点都可以继续find或者findall的操作
li = page.find("li", attrs={"id": "tec"})
# print(li)
'''
<li><a href="http://www.w3.org/Protocols/r"><li>
</li></a></li>'''
a = li.find("a")
print(a)

# 拿到a里的文本 .text 或者.string
# 注意.string只可以提取到标签中直系的内容
# 而.text可以提取到标签中的所有内容
info=a.text
# info=a.string
print(info.strip())
# 技术问题

# 拿到a里的href，其实写起来就像是字典的根据key查找匹配的value

# 方法1
url = a['href']
print(url)
# 方法2
# url=a.get('href')
# print(url)



# b. page.find_all("标签名"[,attrs={"属性":"值"}])  #查找某个元素,且可以指定属性名和属性值，会返回所有匹配的结果,返回的结果是一个列表
head_all = page.find_all('h1', attrs={'id': 'title'})
# print(head_all)

# 拿到所有的链接
page=BeautifulSoup(html,"html.parser")
links=page.find_all('a')
print(links,type(links))
# [<a href="http://www.w3.org/Protocols/r">技术问题</a>, <a href="http://www.baidu.com">非技术问题</a>] <class 'bs4.element.ResultSet'>
for link in links:
    # 打印链接
    print(link.get('href'))
    # 打印文本
    print(link.text.strip())


#