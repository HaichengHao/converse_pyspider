"""
@File    :05demo.py
@Editor  : 百年
@Date    :2025/2/23 21:55 
"""
import execjs

# step 1创建node对象
node = execjs.get()

# step 2编译js文件返回上下文对象
with open('tst.js','r',encoding='utf-8') as fp:
    ctx = node.compile(fp.read())

jsfunc = 'rsa_encryption("123456")'

result = ctx.eval(jsfunc)
print(result)