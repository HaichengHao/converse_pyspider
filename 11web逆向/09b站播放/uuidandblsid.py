"""
@File    :uuidandblsid.py
@Editor  : 百年
@Date    :2025/4/4 20:03 
"""

import execjs
import time
# 封装为一个函数



def getuuid():
    node = execjs.get()
    with open('uuid.js','r',encoding='utf-8') as fp:
        ctx = node.compile(fp.read())  #预加载js文件创建上下文对象
    func_name = 'getuuid()'
    result = ctx.eval(func_name)   #调用js
    # print(result)  #打印输出结果
    return result

# if __name__ == '__main__':
#     getuuid()

def get_blsid():
    node = execjs.get()
    e = int(time.time()*1000)   #创建时间戳对象
    with open('getblsid.js', 'r', encoding='utf-8') as fp:
        ctx = node.compile(fp.read())

    funcname = f'getfinal_t("{e}")'

    res = ctx.eval(funcname)
    # print(res)
    return res
if __name__ == '__main__':
    uuid = getuuid()
    blsid = get_blsid()
    print(uuid,blsid)
