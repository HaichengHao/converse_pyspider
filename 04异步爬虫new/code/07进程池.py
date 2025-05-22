"""
@File    :07进程池.py
@Editor  : 百年
@Date    :2024/12/23 12:12 
"""
# important:导入进程池
from concurrent.futures import ProcessPoolExecutor

# 定义一个函数
def func(name):
    for i in range(20):
        print(name,i)

if __name__ == '__main__':
    with ProcessPoolExecutor(10) as p:
        for i in range(100):
            p.submit(func,f'周杰伦{i}')
#TIPS:在职业生涯中很少能接触到进程池，了解即可，其写法与线程池大体相同，只是进程池开辟的是进程
# 线程池开辟的是线程

#QUIZ:需要思考一个问题:什么时候用多进程什么时候用多线程？
#ANSWER:
# 1.多线程:任务相对统一，任务之间特别的相似
# 2.多进程:多个任务相互独立，很少有交集
# 多进程例子：
# 免费代理ip池
# 1.从各个网站上抓取代理IP
# 2.验证代理IP是否可用
# 3.准备对外的接口
# 三个进程，一个抓，一个验证，一个输送