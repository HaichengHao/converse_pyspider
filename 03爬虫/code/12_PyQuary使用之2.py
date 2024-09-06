0# @Editor    : 百年
# @FileName  :12_PyQuary使用之2.py
# @Time      :2024/7/7 20:37
from pyquery import PyQuery
html = """
<html>
    <div class="aaa">哈哈哈</div>
    <div class="bbb">呼呼呼</div>
</html>
"""
source = PyQuery(html)

# 利用pyquary修改html

# 第一种，普通添加
# a在指定的标签后面添加新的代码
source('div.aaa').after("""<div class="ccc">嘻嘻嘻</div>\n""")
# print(source)
''' 可以看我们修改了原来的html
<html>
    <div class="aaa">哈哈哈</div>
    <div class="ccc">嘻嘻嘻</div>
<div class="bbb">呼呼呼</div>
</html>'''

# 那么有在其后添加就一定可以尝试在其前添加
source('div.aaa').before("""<div class="ddd">geigeigei</div>\n""")
# print(source)
''' 添加成功
<html>
    <div class="ddd">geigeigei</div>
<div class="aaa">哈哈哈</div>
    <div class="ccc">嘻嘻嘻</div>
<div class="bbb">呼呼呼</div>
</html>'''

# 第二种，在标签里边进行添加
source("div.aaa").append("""<span>我愿意喂你</span>""")
# print(source)
'''
<html>
    <div class="ddd">geigeigei</div>
<div class="aaa">哈哈哈<span>我愿意喂你</span></div>
    <div class="ccc">嘻嘻嘻</div>
<div class="bbb">呼呼呼</div>
</html>'''

# 第三种,改写属性值
# 把ccc类的div修改为qqq类
source("div.ccc").attr("class", "qqq")
# print(source)
''' 修改成功
<html>
    <div class="ddd">geigeigei</div>
<div class="aaa">哈哈哈<span>我愿意喂你</span></div>
    <div class="qqq">嘻嘻嘻</div>
<div class="bbb">呼呼呼</div>
</html>'''

# 给qqq添加上新的属性，给它个id，值为138
source("div.qqq").attr("id","138")
# print(source)
"""
<html>
    <div class="ddd">geigeigei</div>
<div class="aaa">哈哈哈<span>我愿意喂你</span></div>
    <div class="qqq" id="138">嘻嘻嘻</div> <--添加成功
<div class="bbb">呼呼呼</div>
</html>"""


# 第四种操作，删除指定的div的属性，以及删除html
# 删除div.qqq的id
source('div.qqq').remove_attr("id")
# print(source)
"""
<html>
    <div class="ddd">geigeigei</div>
<div class="aaa">哈哈哈<span>我愿意喂你</span></div>
    <div class="qqq">嘻嘻嘻</div>
<div class="bbb">呼呼呼</div>
</html>"""

# 删除div.bbb的类属性
source("div.bbb").remove_attr("class")
# print(source)
""" 
<html>
    <div class="ddd">geigeigei</div>
<div class="aaa">哈哈哈<span>我愿意喂你</span></div>
    <div class="qqq">嘻嘻嘻</div>
<div>呼呼呼</div> <--删除成功
</html>"""

# 删除类名为ddd的div,直接删除掉
source("div.ddd").remove()
# print(source)
"""
<html>
                     <-删除成功，直接删掉了这行html代码
<div class="aaa">哈哈哈<span>我愿意喂你</span></div>
    <div class="qqq">嘻嘻嘻</div>
<div>呼呼呼</div>
</html>
"""

# 补充操作，在已经筛选的内容中再次进行筛选
# 前置操作：为了看出效果，新写一段html

html2="""
<html>
    <div class="aaa">
       <p>
           <span>人生</span>
            <span>苟且</span>
       </p>
       <p>
            <span>第几次的蓝天</span>
            <span>influncer</span>
       </p>
        
    </div>
    <div class="bbb">
        <p>
            <span>不可尽欢</span>
            <span>难逃一死</span>
       </p>
        <p>
            <span>第几次的蓝天</span>
            <span>influncer</span>
       </p>
    </div>
    <div class="aaa">
        <p>
            <span>世事无常</span>
            <span>唯有独身</span>
       </p>
        <p>
            <span>第几次的蓝天</span>
            <span>influncer</span>
       </p>
    </div>
</html>
"""
source2=PyQuery(html2)
p=source2('div p span').items()
for item in p:
    # print(item.text())
    # 这时提出需求，只想要第一个
    spaninfo=item('span').eq(0).text()
    print(spaninfo)