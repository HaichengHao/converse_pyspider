import execjs
# import io
# import sys
# import urllib.request
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

# 创建node对象
node = execjs.get()

# 编译js文件返回上下文ctx对象
with open('wanmeishijie.js', 'r', encoding='gb18030') as fp: #important:用utf-8是不行滴!!!mac可能会行
    ctx = node.compile(fp.read())

passwd = "123"
pubkey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCjfeE0MIYsZes/HwV06/kvRw34Hmhn9WPt0feLPp1PVqdqZz1/xFvPPEAJ/lAvfqt5kyn+A06bvYXIhizTjlOzPgLE4897ihuSYXgfwcUshPZvydRLbftU6Exj5SLbv5tw4GInbgQv7RWLWOKyQA81q6lWae2Kcgd1XpDRsQNXVwIDAQAB"

# 确保传递给JavaScript函数的参数是字符串格式
jsfunc = 'getPwd("%s","%s")' % (passwd, pubkey)

try:
    # 尝试运行编译后的JavaScript代码
    result = ctx.eval(jsfunc)
    print(result)
except execjs.RuntimeError as e:
    print("执行JavaScript代码时出错:", e)