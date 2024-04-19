# @Editor    : 百年
# @FileName  :10继承.py
# @Time      :2024/4/19 14:45

# 继承
# 语法格式

'''class 子类类名(父类1，父类2...):
    pass'''
#
# 如果一个类没有继承任何类，则默认继承object
# python支持多继承
# 定义子类时，必须在其构造函数中调用父类的构造函数

# 定义Person类
'''
class Person():
    def __init__(self,name_,age_):
        self.name = name_
        self.age = age_
    def showinfo(self):
        print(f'姓名:{self.name} 年龄:{self.age}')
# 定义一个学生类，继承自Person类，除了有父类的属性外还要有一个学分项
class Student(Person):
    def __init__(self,name_,age_,score_):
        super().__init__(name_,age_) #继承父类的两个属性
        self.score = score_ #还要声明一个父类所不具备的属性，即学分

# 定义一个教师类，继承自Person类，除了父类的属性外还要有一个教龄项
class Teacher(Person):
    def __init__(self,name_,age_,teachofyears_):
        # 先让其继承父类的属性
        super().__init__(name_,age_)
        # 再声明自己所独有的实例属性teachofyears
        self.teachofyears = teachofyears_


# 现在开始创建实例对象
stu1 = Student(name_='张三',age_=20,score_='123')
teacher1 = Teacher(name_='李四',age_=43,teachofyears_='12')

# 调用实例方法
stu1.showinfo()
teacher1.showinfo()
# 姓名:张三 年龄:20
# 姓名:李四 年龄:43
'''
# 观察发现只是调用了Person类中的方法并没有输出学分和教龄，
# 我们可以利用下一节的方法——重写来定义子类要实现的功能


# 关于多继承
class A():
    def __init__(self):
        pass
class B(A):
    def __init__(self):
        pass
class C(A,B): #类C继承自A,B两个类，这就是多继承
    def __init__(self):
        pass