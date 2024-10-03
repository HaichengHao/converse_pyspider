# @Editor    : 百年
# @FileName  :01初识Selenium.py
# @Time      :2024/9/29 22:38

# selenium 可以自动打开一个浏览器
# 输入网址
# 从页面取出东西
import selenium
import requests
from selenium.webdriver import Chrome

# 先创建一个浏览器对象
# executable_path 指定可执行的chromedriver路径
# options= 指定配置信息,目前还用不到
web = Chrome(executable_path='../others/chromedriver.exe')
url = 'https://www.baidu.com'

# 打开url对应的网址,相当于我们在浏览器的搜索框里输入了百度的网址
web.get(url)

# 接下来从文件里提取出一些东西
print(web.title) #我们拿到网页的标题
# 百度一下，你就知道

page_source = web.page_source #通过浏览器对象.page_source可以获取网页的elements的代码,
'''这是与之前的requests为主的所做不到的,相当于你可以直接获得加载后的内容,
即js加载渲染出来的内容,有些网站现在甚至只写一个外部的html，内容全靠js,
 如果用requests获得网页源代码,那么获取的只是一个空空的html'''
# 注意,web.find_element_by_xxx返回的是一个selenium的对象,不是直接的文字内容,需要后面跟上.text属性才可以获得
# 而web.find_elements_by_xxx返回的是一个selenium对象的列表,也是需要对其中每个元素都跟上.text属性才行
# 可以使用遍历每个列表中的selenium.text获得内容