"""
@File    :blsid.py
@Editor  : 百年
@Date    :2025/4/3 23:48 
"""
import execjs
import time
def get_blsid():
    node = execjs.get()
    e = int(time.time()*1000)   #创建时间戳对象
    with open('getblsid.js', 'r', encoding='utf-8') as fp:
        ctx = node.compile(fp.read())

    funcname = f'getfinal_t("{e}")'

    res = ctx.eval(funcname)
    # print(res)
    return res
# if __name__ == '__main__':
#     rest = get_blsid()
#     print(rest)