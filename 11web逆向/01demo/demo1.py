"""
@File    :demo1.py
@Editor  : 百年
@Date    :2025/2/21 19:01 
"""
#step 1先导入包
import execjs
#step 2创建node对象
node = execjs.get()
# step 3编译js文件返回上下文ctx对象（将js代码读取出来然后被compile编译才可以）
fp = open('tst.js','r',encoding='utf-8')
ctx = node.compile(fp.read())

#step 4使用上下文对象ctx调用eval函数执行js文件中的指定函数即可
result = ctx.eval('getPwd("abcdefg")')
print(result)