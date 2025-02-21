"""
@File    :demo2.py
@Editor  : 百年
@Date    :2025/2/21 22:51 
"""
# step 1导入包
import execjs
# step 2创建node对象
node = execjs.get()
#step 3编译js文件返回上下文的ctx对象
fp = open('wec.js','r',encoding='utf-8')
ctx = node.compile(fp.read())

# step 4使用上下文对象调用eval函数执行js文件中的指定的函数
result = ctx.eval('getPwd("12345")')
print(result)
