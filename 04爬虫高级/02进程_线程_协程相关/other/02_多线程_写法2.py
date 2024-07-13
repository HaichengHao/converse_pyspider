# @Editor    : 百年
# @FileName  :02_多线程_写法2.py
# @Time      :2024/7/11 22:47
'''
这种写法是面向对象的写法，需要自己定义一个类来进行线程操作
'''
from threading import Thread
# 定义一个类，继承Thread
class MyThread(Thread):
    # 初始化实例对象方法
    def __init__(self,name):
        # 继承父类对象的属性
        super(MyThread,self).__init__()
        self.name = name
    # 必须重写一个叫run的方法
    def run(self):
        for i in range(10):
            print(self.name,i)
if __name__ == '__main__':
    t1=MyThread('周结论')
    t2=MyThread('王力宏')
    t3=MyThread('张学友')
    t1.run()
    t2.run()
    t3.run()

# todo:注意与01的写法进行比较，两种方案都要掌握
"""
python中对于多线程的写法其实比较简单且宽松
分为以下几步
1 自己定义一个类，继承Thread类 
    class Mythread(Thread):
        初始化实例对象
        指定实例方法
        
2 重写run方法，在run方法中编写需要执行的代码 
class Mythread(Thread):
        初始化实例对象
        指定实例方法
        def run(self):
            功能代码
3 创建线程并执行
"""