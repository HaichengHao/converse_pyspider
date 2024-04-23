# @Editor    : 百年
# @FileName  :15特殊方法之new与init.py
# @Time      :2024/4/21 10:35

# __new__() 与 __init__()
# __new__()是创建对象时用的而__init__()是对对象初始化时用的

class Person():

    def __new__(cls, *args, **kwargs):  # 用于创建对象的
        print('__new__()被调用执行了,cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)  # 调用父类object的特殊方法__new__()
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj

    def __init__(self, name_, age_):  # 对实例对象属性进行初始化的方法
        print('__init__()被调用执行了,self的id值为:{0}'.format(id(self)))
        self.name = name_  # 定义实例属性
        self.age = age_

print('object的类对象的id为{0}'.format(id(object)))
print('Person类对象的id为:{0}'.format(id(Person)))

# 创建person类的实例对象
p1 = Person(name_='张三',age_=20)
print('p1这个person类的实例对象的id为:{0}'.format(id(p1)))

'''
object的类对象的id为140719287805824
Person类对象的id为:1752097992544
__new__()被调用执行了,cls的id值为1752097992544
创建的对象的id为1752099159728
__init__()被调用执行了,self的id值为:1752099159728
p1这个person类的实例对象的id为:1752099159728

Process finished with exit code 0
'''