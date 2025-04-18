"""
@File    :04线程池接收返回值.py
@Editor  : 百年
@Date    :2024/12/21 21:29 
"""
from concurrent.futures.thread import ThreadPoolExecutor
import time


# 如果任务有返回值就需要接受返回值
def func(name, t):  # 再在参数中传入一个t时间变量方便输出的时候观察输出的结果，不必深究
    time.sleep(2)
    time.sleep(t)
    print("我是", name)
    return name  # IMPORTANT:注意这里与上节的不同，这里添加了返回值，而且我们想要接收这个返回值


# 这里我们就需要定义一个函数用来作为任务完成之后的操作
def fn(res):
    print(res.result())  # 函数内指定的操作是打印结果，即打印返回值

'''
if __name__ == '__main__':
    with ThreadPoolExecutor(3) as t:
        
        t.submit(func, f"周杰伦",2).add_done_callback(fn) #IMPORTANT:添加任务完成之后的绑定操作
        t.submit(func, f"王力宏",1).add_done_callback(fn)
        t.submit(func, f"王富贵",3).add_done_callback(fn)
        '''
# IMPORTANT:返回callback执行的顺序是不确定的,返回值的顺序是不确定的
'''
我是 王力宏
王力宏 <--确实是都打印了返回值，注意add_done_callback(fn)有一个现象，那就是任务完成之后立即执行  
我是 周杰伦
周杰伦
我是 王富贵
王富贵
'''

# QUIZ: 如何改善上面的代码？
# ANSWER:利用map映射解决,map(func,iterable)
#  它能够不用写太多代码，，只需要将传入的参数组成列表这种可迭代的类型然后传入到func中即可
if __name__ == '__main__':
    with ThreadPoolExecutor(3) as t:
        # IMPORTANT:如果忘记了就回看python基础的37,内置函数（下）
        result = t.map(func,['周杰伦','王力宏','王富贵'],[2,1,3]) #tips:map(函数/匿名函数,可迭代对象,参数)
        print(type(result))
#  <class 'generator'> <--注意Result的类型是生成器
# 我是 王力宏
# 我是 周杰伦
# 我是 王富贵
        for r in result:
            print(r)
            '''
            周杰伦
            王力宏
            王富贵 返回的结果的顺序是任务分发的顺序'''
#IMPORTANT:map返回值是生成器，返回的内容和任务分发的顺序是一致的
# TIPS: 如果想利用多线程的效果得到一个有序的返回值结果就可以用map,如果对返回的顺序没有要求那就跟之前的一样subbmit就行了
