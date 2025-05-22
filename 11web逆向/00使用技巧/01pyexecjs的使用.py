"""
@File    :01pyexecjs的使用.py
@Editor  : 百年
@Date    :2025/5/22 19:09 
"""
# 开始之前 pip install pyexecjs
#
# #answer:在python中链接CMD的那个东西是subprocess里面的Popen,注意一下代码要写在引入execjs之前

import subprocess
from functools import partial #tips:partial(偏函数)用来锁定某个参数的固定值,我们现在想要的就是锁定Popen中的初始化实例对象的encoding
subprocess.Popen = partial(subprocess.Popen,encoding='utf-8') #锁定要修改的函数,指定要修改的属性并指定值
import execjs

from  subprocess import Popen


#step1:创建节点对象(获得节点对象)
print(execjs.get().name) #打印引擎的名字
# node = execjs.get()
#step2:读取js文件
with open('./jsfile/demo1.js','r',encoding='utf-8') as fp:
    #step3:创建上下文对象
    # ctx = node.compile(fp.read())
    ctx = execjs.compile(fp.read())
#step4:利用上下文对象调用js中的方法
res = ctx.eval("a1(1,'你好')")
res2 = ctx.eval('a2("hello","棒子鸡")')
print(res)
print(res2)

# cmd默认的字符集是gbk,所以传入文字的会被转成gbk,但python里写的是utf-8,所以会乱码
#QUIZ:如何解决?
#answer: 可以指定字符集的设置

