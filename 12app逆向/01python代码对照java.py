"""
@File    :01python代码对照java.py
@Editor  : 百年
@Date    :2025/3/30 12:38 
"""

class Mytest:
    # 绑定方法，需要创建实例对象，然后通过实例对象调用
    def f1(self):
        print("f1被调用了")
    # 静态方法,不需要创建实例对象就可以直接调用
    @staticmethod
    def f2():
        print("f2被调用了")
    def f3(self):
        return "f3被调用咯"

if __name__ == '__main__':

    # 创建实例对象调用绑定方法
    obj = Mytest()
    obj.f1()
    # 尝试不通过实例对象调用类方法
    try:
        Mytest.f1()
    except BaseException as e:
        print(e)
    # '绑定方法是不能直接被类名.方法名调用的哦!!!'
    # 静态方法可以直接通过类名调用
    Mytest.f2()
    f3_runtimeresult = obj.f3()
    print(f3_runtimeresult)

'''
f1被调用了
Mytest.f1() missing 1 required positional argument: 'self'
f2被调用了'''