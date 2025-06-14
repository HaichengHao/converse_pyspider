"""
@File    :01启动和接管浏览器.py
@Editor  : 百年
@Date    :2025/6/1 16:01 
"""
'''
顾名思义，ChromiumPage是 Chromium 内核浏览器的页面，使用它，我们可与网页进行交互
，如调整窗口大小、滚动页面、操作弹出框等等。还可以跟页面中的元素进行交互，如输入文字、
点击按钮、选择下拉菜单、在页面或元素上运行 JavaScript 代码等等。
可以说，操控浏览器的绝大部分操作，都可以由ChromiumPage及其衍生的对象完成，而它们的功能，
还在不断增加。除了与页面和元素的交互，ChromiumPage还扮演着浏览器控制器的角色，可以说，
一个ChromiumPage对象，就是一个浏览器。
'''

# tips:
'''
# 用ChromiumPage()创建页面对象。根据不同的配置，可以接管已打开的浏览器，
# 也可以启动新的浏览器。程序结束时，被打开的浏览器不会主动关闭，以便下次运行程序时使用
# （由 VSCode 启动的会被关闭）。

# 这种方式代码最简洁，程序会使用默认配置，自动生成页面对象。
# 创建ChromiumPage对象时会在指定端口启动浏览器。默认情况下，程序使用 9222 端口。
'''
from DrissionPage import ChromiumPage
# page = ChromiumPage()

#指定端口启动浏览器
#启动9333端口的浏览器，如该端口关闭,启动一个新的浏览器
# page1 = ChromiumPage(9333)

#接管浏览器
'''
当页面对象创建时，只要指定的端口port已有浏览器在运行，就会直接接管。
无论浏览器是哪种方式启动的。比如：先通过如下代码启动一个端口为8866的浏览器'''

page2 = ChromiumPage(8866)

#在启动的8866的浏览器中,手动访问百度页面,然后使用如下程序测试是否可以接管该浏览器

print(page2.title,page2.url)
