"""
@File    :02多线程写法2(面向对象).py
@Editor  : 百年
@Date    :2024/12/21 20:44 
"""
# IMPORTANT:注意，在爬虫程序中一般不这么写
# 对于面型对象多线程的写法python只有简单的规定，即自己写一个类继承Thread并重写run方法
from threading import Thread

# 自定义一个类来继承Thread
class MyThread(Thread):
    # 初始化实例对象
    def __init__(self,name):
        super().__init__() #先继承父类Thread的属性
        self.name = name #再添加一个新的属性
    def run(self):
        for i in range(100):
            print(self.name,i)

if __name__ == '__main__':
    t1 = MyThread("周杰伦")
    t2 = MyThread("周润发")
    t3 = MyThread("周星驰")
    t1.start()
    t2.start()
    t3.start()

