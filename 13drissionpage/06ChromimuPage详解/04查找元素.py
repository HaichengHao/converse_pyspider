"""
@File    :04查找元素.py
@Editor  : 百年
@Date    :2025/6/1 22:34 
"""
'''
查找语法能用于指明以哪种方式去查找指定元素，定位语法简洁明了，熟练使用可大幅提高程序可读性
'''

from DrissionPage import ChromiumPage,ChromiumOptions

opt1 = ChromiumOptions().set_paths(local_port=9111,user_data_path=r'D:\Chromeopts\data1')

page = ChromiumPage(addr_or_opts=opt1)

page.get('https://movie.douban.com/top250')


#基本语法:ele与eles 和selenium中的 find_element find_elements的差不多

# page.ele：只能定位满足要求第一次出现的标签
#
# page.eles：定位到满足要求所有的标签

#利用类属性进行定位
first_title = page.ele('@class=title')
first_title = page.ele('.title') #这样写也是可以的

#利用文本进行定位

# tag1 = page.ele('@text()=选电影')
# tag1.click()

# #当需要多个条件同时确定一个元素时，每个属性用'@@'开头。
# tag2 = page.ele('@@class=bd@@text()=希望让人自由。')
# print(tag2.text)

#当需要以或关系条件查找元素时，每个属性用'@|'开头。
tag3 = page.eles('@|id=row1@|id=row2')


print(first_title.text)


'''

#当需要以或关系条件查找元素时，每个属性用'@|'开头。
tag4 = page.eles('@|id=row1@|id=row2')  # 查找所有id为row1或id为row2的元素

#表示模糊匹配，匹配含有指定字符串的文本或属性。
tag5 = page.eles('@id:ow')  # 获取id属性包含'ow'的元素

#表示匹配开头，匹配开头为指定字符串的文本或属性。
tag6 = page.eles('@id^row')  # 获取id属性以'row'开头的元素

#表示匹配结尾，匹配结尾为指定字符串的文本或属性。
tag7 = page.ele('@id$w1')  # 获取id属性以'w1'结尾的元素





'''