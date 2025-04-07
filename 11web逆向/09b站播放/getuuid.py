"""
@File    :getuuid.py
@Editor  : 百年
@Date    :2025/4/3 16:01 
"""
import execjs
#
# node = execjs.get()
#
#
# with open('uuid.js','r',encoding='utf-8') as fp:
#     ctx = node.compile(fp.read())  #预加载js文件创建上下文对象
#
#
# func_name = 'getuuid()'
#
# result = ctx.eval(func_name)   #调用js
# print(result)  #打印输出结果


# 封装为一个函数



def getuuid():
    node = execjs.get()
    with open('uuid.js','r',encoding='utf-8') as fp:
        ctx = node.compile(fp.read())  #预加载js文件创建上下文对象
    func_name = 'getuuid()'
    result = ctx.eval(func_name)   #调用js
    print(result)  #打印输出结果
    return result

if __name__ == '__main__':
    getuuid()