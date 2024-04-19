# @Editor    : 百年
# @FileName  :07python中的权限控制.py
# @Time      :2024/4/18 17:22

# 权限控制是通过对属性或方法添加单下划线、双下划线以及首尾双下划线来实现
# 单下划线开头以单下划线开头的属性或方法表示protected受保护的成员，这类成员被视为仅供内部使用，允许类本身和子类进行访问，但实际上它可以被外部代码访问
# 双下划线开头表示private私有成员，这类成员只允许定义该属性或方法的类本身进行访问
# 首尾双下划线一般表示特殊方法

class Student():
    def __init__(self, name, age, gender):  # 这里就用到了首尾双下划线的init，
        self._name = name  # 这里在实例属性前加一个单下划线表示这个实例属性为被保护的属性，只能够本类和子类访问
        self.__age = age  # 表示私有类，只能类本身来访问
        self.gender = gender  # 普通的实例属性，可以在类的内部，外部以及其子类都可访问

    def _func1(self):  # 定义了一个受保护的对象，只能其子类和其本身使用
        print('我是受保护的对象，只能我自己或者我的子类访问，但是我其实也可以被外部访问')

    def __func2(self):  # 定义一个私有对象，只有定义的可以被访问
        print('只有定义的类可以被访问')

    def show(self):
        print('我是一个普通的实例方法')
        # 类本身可以使用受保护的方法
        self._func1()  # 普通的实例方法可以使用受保护的方法
        # 类本身可以使用私有的方法
        self.__func2()
        # 类本身可以使用受保护的属性和私有的实例属性
        print(self._name, self.__age)

# 我们现在在类的外部了
# 创建一个实例对象stu1,其属于Student类，传入三个属性的值
stu1 = Student(name='张三', age=20, gender='male')
try:

    # todo:注意一个一个来验证，方便理解
    # 在类的外部访问受保护的属性,实际上可以被类的外部访问
    # print(stu1._name)

    # 尝试访问私有的属性
    # print(stu1.__age)
    # 'Student' object has no attribute '__age' <--可以发现私有属性不能被外部访问，只可以在其类本身中被访问

    #尝试在Student类的外部访问被保护的方法
    # stu1._func1()
    # 我是受保护的对象，只能我自己或者我的子类访问，但是我其实也可以被外部访问 <--发现其也是可以在类的外部使用的

    #尝试访问私有的方法
    stu1.__func2()
#     'Student' object has no attribute '__func2'  <--可以发现私有的方法是不可在Student类的外部进行访问的

except BaseException as e:
    print(e)

# 思考：难道私有的属性和方法真的不能够在类的外部进行访问吗？
# 不是的，是可以被外部访问的
# 语法格式
# 实例对象名称._类名__私有属性/方法的名称

print(stu1._Student__age)
# 20 <--访问成功

# 按照上面的思路，我们尝试访问私有方法
stu1._Student__func2()
# 只有定义的类可以被访问 <--成功!
print(dir(stu1))
# '_func1', '_name', 'gender', 'show'] <--这里也是只截取后面的部分，可以看到stu1具有的属性和方法，其实其本身是不可以直接拥有私有的属性和方法的
# 所做的访问私有的属性和方法的操作，其实是越权操作
