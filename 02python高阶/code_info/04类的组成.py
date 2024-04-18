# editor: 百年
# time: 2024/4/18 9:29
class Person(): #定义一个类，默认继承object类，可以不写
    death = 'moral to die' #给Person指定一个类属性，类属性在类中，方法之外
    def __init__(self,name,age): #初始化实例对象，即对实例属性进行定义,其中name,age是方法的参数，是局部变量，它们的作用域是整个__init__
        self.name = name  #实例属性定义在__init__()方法之中，使用self进行打点
        self.age = age #左侧是实例属性，右侧是局部变量，将局部变量的值(等号右侧)赋给实例属性(等号左侧)
# 实例属性的名称和局部变量的名称可以相同，但是要搞清楚，右边是局部变量左边是实例属性
# 定义实例方法
#     定义在类中的函数称为方法，自带一个参数self
    def show(self):
        # 注意，实例属性是可以在整个类当中被调用的
        print(f'我叫{self.name},我今年{self.age}岁了')
    @staticmethod
    def sm():
        print('我是个静态方法在静态方法中不能调用实例属性和实例方法')

    # 定义静态方法
    # try:
    #     print(self.show())
    # except BaseException as e:
    #     print('实例方法未能被调用')
    # try:
    #     print(self.name)
    # except BaseException as e:
    #     print('实例对象未被调用')
    # Person.sm() #尝试调用观察是不是静态方法真的不能够调用实例属性

# 定义类方法
    @classmethod
    def cm(cls): #cls --> class的简写
        print('这是一个类方法')
   # 尝试类方法能否调用实例属性和实例方法
    try:
        print(self.name)
    except BaseException as e:
        print('类方法中不可调用实例属性')
    try:
        print(self.show())
    except BaseException as e:
        print('类方法中不能调用实例方法')

'''
类方法中不可调用实例属性
类方法中不能调用实例方法
'''


'''
这是一个静态方法，在静态方法中不能调用实例属性和实例方法
实例方法未能被调用
实例对象未被调用
观察发现静态方法不能调用实例属性'''

# 创建实例对象
# 语法： 实例对象名=类名(实例对象属性指定)
person1=Person(name='张三',age=18) #我们在初始化实例属性的时候指定了Person所具有的2个属性即姓名以及年龄

# 实例属性，使用对象名进行打点调用的
print(f'姓名:{person1.name},年龄:{person1.age}')
# 姓名:张三,年龄:18 <--输出成功
# 类属性可以直接使用类名进行打点调用
print(f'人类共有的类属性{Person.death}',end='')
# 人类共有的类属性moral to die <--凡人总有一死


# 调用实例方法
person1.show() #因为person1是我们创建的实例对象，那么就可以调用实例方法

# 调用类方法
Person.cm()

# 调用静态方法

Person.sm()