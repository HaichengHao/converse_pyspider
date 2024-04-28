# @Editor    : 百年
# @FileName  :16组合.py
# @Time      :2024/4/24 10:00
'''
之前学了继承，继承是什么关系呢？ 继承是'is-a'关系，例如猫是个动物，狗也是个动物
那么组合是 'has-a'关系，例如手机有cpu,也有屏幕，就是这样的has-a的关系
'''
class A1:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("a1 say"+self.name) #实例属性可以在类的作用域内被访问
class B1(A1):
    pass
# B1类继承了A1类，那么通过创建B1类的实例对象就可以使用A1的方法

b_1 = B1(name='张三')
b_1.say()

class A2:
    def say(self):
        print('a2 say')
class B2:
    def __init__(self,a):
        self.a = a
#创建一个属于A2类的实例对象
a_2 = A2()
# 将a_2作为参数传入B2中创建实例对象b_2
b_2  = B2(a_2)
b_2.a.say()
# a2 say