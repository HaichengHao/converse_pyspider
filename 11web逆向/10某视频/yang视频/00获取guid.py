"""
@File    :00获取guid.py
@Editor  : 百年
@Date    :2025/4/18 14:57 
"""

import execjs

'''
# 创建节点
node = execjs.get()

# 读取js文件
with open('../js逆向/getuid.js','r',encoding='utf-8') as fp:
    ctx = node.compile(fp.read())

# 调用函数
funcName = 'getuid()'
uid = ctx.eval(funcName)
# 打印结果
print(uid)

'''

# important:换一种方式来写，之前写的总是要读取js文件也是烦人的不行
# tips:指定js代码
body="""
    function getuid() {
           var e ="";
                var t = Date.now().toString(36)
                  , r = Math.random().toString(36).replace(/^0./, "");
                e = "".concat(t, "_").concat(r);
            return e
        }
"""
# tips:不用创建节点了，直接调用Execjs对其进行编译
JS_ = execjs.compile(body)
guid = JS_.call('getuid') #调用函数
print(guid)
