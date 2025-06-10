"""
@File    :选择定位语法.py
@Editor  : 百年
@Date    :2025/6/1 22:54 
"""



from DrissionPage import ChromiumPage,ChromiumOptions

opt1 = ChromiumOptions().set_paths(local_port=9111,user_data_path=r'D:\Chromeopts\data1')

page = ChromiumPage(addr_or_opts=opt1)

page.get('https://movie.douban.com/top250')

#class定位语法
title = page.ele('.title')
title = page.ele('.=title') #同上
title = page.ele('.:tit') #查找class属性包含_tit的元素
title = page.ele('.^tit_') #查找class以tit为开头的元素
title = page.ele('.$_tle') #查找classs以tle为结尾的元素


#id定位器语法
content = page.ele('#content')
content = page.ele('#=content')
content = page.ele('#:cont')  #查找id属性包含cont的
content = page.ele('#^co') #查找co开头的id属性
content = page.ele('#$tent') #查找tent结尾的


#xpath定位
content = page.ele('xpath://div[@id="content"]')

#标签元素定位
ele1 = page.ele('tag:div')  # 查找第一个div元素
ele2 = page.ele('tag:p@class=p_cls')  # 与单属性查找配合使用
ele3 = page.ele('tag:p@@class=p_cls@@text()=第二行')  # 与多属性查找配合使用

#文本定位
element1 = page.ele('text=第二行')  # 查找文本为“第二行”的元素
element2 = page.ele('text:第二')  # 查找文本包含“第二”的元素
element3 = page.ele('第二')  # 与上一行一致