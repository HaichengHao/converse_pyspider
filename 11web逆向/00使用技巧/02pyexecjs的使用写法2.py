"""
@File    :02pyexecjs的使用写法2.py
@Editor  : 百年
@Date    :2025/5/22 19:47 
"""

import execjs
#step1:读取js文件
fp = open('./jsfile/demo1.js','r',encoding='utf-8')

#step2:调用execjs去加载所有的js文件
js_code = fp.read()
js = execjs.compile(js_code)

#step3:调用编写的函数
# res = js.eval("a1(1,5)")
res = js.call('a1',1,5) #或者这种调用方式
print(res)

