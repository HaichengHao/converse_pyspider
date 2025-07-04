"""
@File    :04设置代理.py
@Editor  : 百年
@Date    :2025/7/3 19:07 
"""
from DrissionPage import SessionPage,SessionOptions

#important:如果需要在使用前进行一些配置，可使用`SessionOptions`。它是专门用于设置`Session`对象初始状态的类，内置了常用的配置。


# 在`SessionPage`创建时，将已创建和设置好的`SessionOptions`对象以参数形式传递进去即可。

seesion_opt = SessionOptions().set_proxies(http='xxx')

page = SessionPage(session_or_options=seesion_opt)


# 可以把配置保存到配置文件以后自动读取
