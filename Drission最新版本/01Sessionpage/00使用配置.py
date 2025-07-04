"""
@File    :00使用配置.py
@Editor  : 百年
@Date    :2025/7/3 19:18 
"""
'''
`SessionPage`对象和`WebPage`对象的 s 模式都能收发数据包
，本节只介绍`SessionPage`的创建，在`WebPage`的章节再对其进行介绍。'''

from DrissionPage import SessionPage,SessionOptions
# page = SessionPage(session_or_options=None,timeout=None)
#tips:初始化参数解释
# `session_or_options` 传入`Session`对象时使用该对象收发数据包；传入`SessionOptions`对象时用该配置创建`Session`对象；为`None`则从 ini 文件读取

'''
`SessionPage`无需控制浏览器，无需做任何配置即可使用。

直接创建时，程序默认读取 ini 文件配置，如 ini 文件不存在，会使用内置配置。

默认 ini 和内置配置信息详见“进阶使用->配置文件的使用”章节。
如果需要在使用前进行一些配置，可使用`SessionOptions`。
它是专门用于设置`Session`对象初始状态的类，内置了常用的配置。详细使用方法见“启动配置”一节。
'''

# 创建配置对象,并设置代理信息
session_opt = SessionOptions().set_proxies(http='127.0.0.1:1080')

# 用该配置创建页面对象
page = SessionPage(session_or_options=session_opt)
# 您可以把配置保存到配置文件以后自动读取，详见”启动配置“章节。


'''
以上方法是使用默认 ini 文件中保存的配置信息创建对象，你可以保存一个 ini 文件到别的地方，并在创建对象时指定使用它。
'''

session_opts1 = SessionOptions(ini_path=r'./config1.ini')
# 使用该配置对象创建页面

page = SessionPage(session_or_options=session_opts1)


# 不使用 ini 文件
session_opts2 = SessionOptions(read_file=False)

session_opts2.set_retry(5)
page = SessionPage(session_or_options=session_opts2)

# 传递控制权
'''
当需要使用多个页面对象共同操作一个页面时，可在页面对象创建时接收另一个页面间对象传递过来的`Session`对象，
以达到多个页面对象同时使用一个`Session`对象的效果。'''

# 创建一个页面
page1 = SessionPage()
# 获取页面对象内置的Session对象
session = page1.session
# 在第二个页面对象初始化时传递该对象
page2 = SessionPage(session_or_options=session)




