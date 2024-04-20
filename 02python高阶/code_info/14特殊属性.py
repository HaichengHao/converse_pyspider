# @Editor    : 百年
# @FileName  :14特殊属性.py
# @Time      :2024/4/20 9:38

# print(dir(object))  # 查看object类中的属性和方法

# ['__class__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__']
class A:
    pass

class B:
    pass

class C(A,B): #继承A,B两个类
    def __init__(self,name_,age_): #初始化实例属性
        self.name = name_
        self.age = age_

c1 = C(name_='张三',age_=20)


# 利用特殊属性.__dict__获得类对象或实例对象的所有属性和方法的字典

#查看C类的类对象的属性字典
print(C.__dict__)
# {'__module__': '__main__', '__init__': <function C.__init__ at 0x00000248F130E290>, '__doc__': None}

print(c1.__dict__) #打印实例对象的属性字典
#{'name': '张三', 'age': 20}

# 利用__class__可以查看指定对象所属的类
print(c1.__class__)
# <class '__main__.C'>

# 利用__bases__可以查看一个类的所有父类，返回值时一个元组
print(C.__bases__)
# (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)
# <class '__main__.A'> 注意，谁写在前就输出谁

# 利用__mro__输出类的层次结构，返回值是一个元组
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# 特殊方法__subclasses__()，返回指定的类的子类，返回值是一个列表
print(A.__subclasses__())
# [<class '__main__.C'>]

print(C.__subclasses__())
# [] <--如果指定的类没有子类，则返回一个空列表