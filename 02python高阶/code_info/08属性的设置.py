# @Editor    : 百年
# @FileName  :08属性的设置.py
# @Time      :2024/4/19 11:02

# 在这里可以结合基础篇中的装饰器迭代器进行对比学习

class Student():
    def __init__(self,name_,age_,gender_):#初始化实例对象
        self.name = name_
        self._age = age_
        self.__gender = gender_ #将性别设置为私有属性
#       上一小结我们学了如何强制访问私有的属性或者方法，但是是不推荐的
#       我们其实可以使用装饰器将方法转成属性来使用
    @property #利用property装饰器去修饰方法，可以先看看其builtins
    def gender(self): #把要装饰的私有方法写到装饰器下面
        return self.__gender #注意，它是有返回值的，返回的是私有属性本身
    @gender.setter #将私有属性gender设置为可写对象
    def gender(self,value):
        if value !='male' and value != 'female':
            print('输入错误，已将性别默认设置为male')
            self.__gender = 'male'
        else:
            self.__gender = value
# 创建Student类的对象
stu1 = Student(name_='张三',age_=10,gender_='male')

# 尝试访问实例属性中的私有属性
print(stu1.gender)
# male <--访问成功，说明利用@property这样的装饰器装饰后，私有的方法也是可以像普通的实例方法那样被外部访问的

# 尝试修改属性值
try:
    stu1.gender = 'female'
    print(stu1.gender)
except BaseException as e:
    print(e)
    # can't set attribute 'gender' <--可以发现，虽然可以进行外部访问，但是私有属性是不可以进行修改的
    # 那么有办法进行修改吗？，我们只需要将私有属性设置为可写属性即可，见第17行
    # 设置完可写属性后再次运行
    # female <--发现修改成功