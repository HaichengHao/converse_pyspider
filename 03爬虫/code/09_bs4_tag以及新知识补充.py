# @Editor    : 百年
# @FileName  :09_bs4_tag.py
# @Time      :2024/7/1 10:04
from bs4 import BeautifulSoup
'''
# 原始 HTML 文本
fp = open('../../pycharm常用快捷键.html','r',encoding='utf-8')

# 实例化BeautifulSoup对象，然后把即将被解析的页面源码数据加载到了该对象(page_source)当中
page_source=BeautifulSoup(fp,'lxml') #参数'lxml'是固定形式表示指定的解析器，当然也可以使用08使用的html.parser
# print(page_source)

#1 标签定位  实例化对象.tagName 指挥定位到符合条件的第一个标签

# 利用tag输出文件的title,当然，我们只要其中的文字，所以利用.text取出其中的文字即可
print(page_source.title.text)
'''
# 2属性定位 实例化对象名.find('目标标签'[,指定属性以及值])

'''fp=open('../others/tst.html','r',encoding='utf-8')
page_source=BeautifulSoup(fp,'lxml')
title=page_source.find('title')
print(title.text)

# 找到类名为name的所有a标签并输出其文字内容
# 我们可以看到和08学的相比，08是使用了attrs={'属性名':'属性值'}这样的可选参数，而这里是 属性名_='属性值'这样的方式，注意属性名后面跟了一个下划线
bookinfo=page_source.find_all('a',class_='name') #注意在python官方文档(按住ctrl选择要查看的属性)中写有这个find_all和findAll是一样的，直接写了等号
print(bookinfo)
for book in bookinfo:
    print(book.text)'''
'''
阳小戎
踏雪真人
阎ZK
古羲
宅猪
沙拉古斯
夜南听风
周一口鸟
三五玄七
历史里吹吹风
烽仙
康斯坦丁伯爵
仁者为鬼
长鲸归海
爱潜水的乌贼
雨去欲续
裴不了
季越人
黑山老鬼
常世

Process finished with exit code 0
'''


# 3 选择器定位(结合前端知识进行理解)
'''
回顾前端知识
id选择器 #id值
类选择器  .类名
层级选择器 >代表子代 ，空出空格代表子孙选择器'''

fp=open('../others/id选择器.html','r',encoding='utf-8')
page_source=BeautifulSoup(fp,'lxml')
# 1id选择器查找

# 找到所有id为water的标签
# target=page_source.select('#water')
# print(target)
# [<h4 id="water">哪怕好多盆水往下淋</h4>] 《--注意返回值仍然是一个列表
# print(target[0].text)
# 哪怕好多盆水往下淋


# 找到类名为loveu的所有标签
'''tag2=page_source.select('.loveu')
print(tag2)
#[<h1 class="loveu">天空好像下雨，我好想住你隔壁</h1>, <h2 class="loveu">傻站在你家楼下抬起头数乌云</h2>] 《--同样的，返回的是匹配规则的所有元素组成的列表，想要拿到文本依旧是需要正确的操作

for item in tag2:
    print(item.text)'''
'''
天空好像下雨，我好想住你隔壁
傻站在你家楼下抬起头数乌云'''


# 找到id为ep1下的所有p标签
'''tag3=page_source.select('#ep1 p')
print(tag3)
# [<p>夏天快要过去</p>, <p>请你少买冰淇淋</p>]

# 补充,对于tag取值可以利用.string的方式
for tag in tag3:
    # print(tag.string)
    print(tag.text)'''
'''
夏天快要过去
请你少买冰淇淋'''


# 获取标签中的属性名和属性值,和08的差不多
src=page_source.img
print(src['src'])
fp.close()


