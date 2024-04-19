# @Editor    : 百年
# @FileName  :11方法重写.py
# @Time      :2024/4/19 15:55
# 如果子类对继承自父类的某个属性或者方法不满意，可以在其子类中对其(方法体)进行重新编写
# 子类重写后的方法可以通过super().xxx()调用父类中被重写的方法

# 利用继承那节的代码来进行对比学习
class Person():
    def __init__(self,name_,age_):
        self.name = name_
        self.age = age_
    def showinfo(self):
        print(f'姓名:{self.name} 年龄:{self.age}',end=' ') #这里加上不换行是为了调用重写的方法时候能够美观些
# 定义一个学生类，继承自Person类，除了有父类的属性外还要有一个学分项
class Student(Person):
    def __init__(self,name_,age_,score_):
        super().__init__(name_,age_) #继承父类的两个属性
        self.score = score_ #还要声明一个父类所不具备的属性，即学分

#     开始重写父类中的方法 其实ide会给出提示Overwrite method in Person 表示Person类中的方法被重写
    def showinfo(self):
        super().showinfo() #首先调用父类中的方法，
#         然后再加上自己新定义的功能实现代码
        print(f'学分:{self.score}')
# 定义一个教师类，继承自Person类，除了父类的属性外还要有一个教龄项
class Teacher(Person):
    def __init__(self,name_,age_,teachofyears_):
        # 先让其继承父类的属性
        super().__init__(name_,age_)

        # 再声明自己所独有的实例属性teachofyears
        self.teachofyears = teachofyears_
    def showinfo(self): #重写父类的方法
        super().showinfo() #首先先继承需要用到的父类中的方法
#         然后再加上自己新增的功能代码
        print(f'教龄:{self.teachofyears}')

# 现在开始创建实例对象
stu1 = Student(name_='张三',age_=20,score_='123')
teacher1 = Teacher(name_='李四',age_=43,teachofyears_='12')

# 调用实例方法
stu1.showinfo()
# 姓名:张三 年龄:20 学分:123 <--发现我们进行重写后在不影响原始父类方法实现的基础上增加了新的功能，非常舒服

teacher1.showinfo()
# 姓名:李四 年龄:43 教龄:12

