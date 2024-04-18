# editor: 百年
# time: 2024/4/18 8:15
# Python和java是面向对象的语言
# 类是一个抽象的模板
'''自定义数据类型的语法格式为
class 类名(object):
'''
'''
创建对象的语法格式为:
对象名 = 类名()
对象:即属于某一类的具体实例
譬如车子是一个大类，又包含多个对象，如推土车，卡车货车小轿车这种具体的区分'''
# 定义一个Person类，包含姓名和年龄
# 注意，类名首字母一般大写
# 定义一个类，名称为Person
class Person(object): #默认继承object类，其中的object可以省略
    def __init__(self,name,age): #初始化实例对象
        self.name=name #实例对象的属性指定
        self.age=age

# 定义猫科动物类
class Cat(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#定义犬科动物类
class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#定义学生类
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

# 创建自定义类型的对象 创建语法 对象名 = 类名()
# 创建一个学生对象stu1
stu1 = Student(name="张胜男",age=19)
# 创建一个对象，属于猫科动物类
cat1=Cat(name="hellokitty",age=10)


# 可以查看创建的对象属于哪种类型
print(type(cat1))
print(type(stu1))
'''
<class '__main__.Cat'>
<class '__main__.Student'>
可以看出其确实属于了我们自己指定的类型'''