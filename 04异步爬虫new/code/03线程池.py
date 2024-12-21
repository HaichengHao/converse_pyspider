"""
@File    :03线程池.py
@Editor  : 百年
@Date    :2024/12/21 21:09 
"""
#QUIZ:什么是线程池？
#ABST:线程池是将多个任务中的多个线程放到以一个类似与水池的概念的东西里面，
# 它会自动从水池里拿出线程，只要有空余空间就放进去，满了就会在拿出的线程处理完毕之后再拿出新的线程



# 导入线程池执行器
from concurrent.futures import ThreadPoolExecutor

def func(name):
    for i in range(10):
        print(name,i)

if __name__ == '__main__':
    # 开辟大小为10的线程池
    with ThreadPoolExecutor(10) as t:
        for i in range(100):
            t.submit(func,f"周杰伦{i}") #IMPORTANT:100个任务交给大小为10的线程池

    # 最多十个任务




