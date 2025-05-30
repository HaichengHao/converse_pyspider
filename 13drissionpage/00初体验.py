# @Author    : 百年
# @FileName  :00初体验.py
# @DateTime  :2025/5/30 19:01

'''
在DrissionPage框架中，有一个非常重要的工具叫做“页面类”，主要用于控制浏览器 和 收发数据包。
DrissionPage 包含三种主要页面类。我们可以根据自己的需要选择使用。
'''

#tips:如果只要控制浏览器,导入ChromiumPage

from DrissionPage import ChromiumPage

#tips:如果只要收发数据包，导入SessionPage。
from DrissionPage import SessionPage

#tips:WebPage是功能最全面的页面类，既可控制浏览器，也可收发数据包。
from DrissionPage import WebPage

'''
如果只使用收发数据包功能，无需任何准备工作。
如果要控制浏览器，需设置浏览器路径。程序默认设置控制 Chrome，所以下面用 Chrome 演示。
开始前，我们先设置一下浏览器路径。
程序默认控制 Chrome，所以下面用 Chrome 演示。 如果要使用 Edge 或其它 Chromium 内核浏览器，设置方法是一样的。

'''
page = ChromiumPage()
page.get('https://www.baidu.com')


