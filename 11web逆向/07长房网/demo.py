# @Author    : 百年
# @FileName  :demo.py.py
# @DateTime  :2025/3/24 14:12

import execjs
# step 1 创建node对象
node = execjs.get()
# step 2 读取js文件创建上下文对象
with open('cfw_0.js','r',encoding='utf-8') as fp:
    ctx = node.compile(fp.read())
funcname = f'getPwd("123456")'
# step 3 调用上下文加载函数
result = ctx.eval(funcname)
print(result)

