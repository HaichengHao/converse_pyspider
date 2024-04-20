# @Editor    : 百年
# @FileName  :12object类.py
# @Time      :2024/4/19 16:17
# Object 类
# * object类是所有类的父类，因此所有类都有object类的属性和方法<br>
# * 内置函数dir()可以查看指定对象所有属性
# * object有一个__str__()特殊方法，用于返回一个对于`"对象的描述"`,
# 对应与内置函数str()经常用于print()方法，帮助我们查看对象的信息,
# 所以我们经常会对__str__()进行重写

class Student:
    def __init__(self,name_,age_):
        self.name = name_
        self.age = age_
    def __str__(self): #对__str__()进行重写
        return '我叫{0},今年{1}岁'.format(self.name,self.age)

stu1 = Student(name_='张三',age_=12)
print(stu1) #重写__str__()后，执行语句会默认执行Object类中的__str__()方法
# 如果未对__str__()方法进行重写，那么这里输出的就是stu1的内存地址<__main__.Student object at 0x0000012E8E328A00>
# 而重写之后这里的输出结果为
# 我叫张三,今年12岁