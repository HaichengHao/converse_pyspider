# @Editor    : 百年
# @FileName  :06动态绑定属性和方法.py
# @Time      :2024/4/18 16:58
#每个对象的属性名称相同，但是属性值不同
#可以为某个对象绑定独有的属性或方法
def self_intc():
    print('我是定义在类之外的一个函数，这时候叫我函数比较好，我可以被动态绑定从而成为一个实例变量的放法')
class Student():
    school = 'bilibili大学'
    def __init__(self,name_,age_):
        self.name = name_
        self.age = age_
    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'姓名:{self.name},年龄:{self.age}')
# 创建两个student类的对象
stu1 = Student(name_= '张三',age_=18)
stu2 = Student(name_ = '李四',age_=20)

# 为stu2动态绑定一个实例属性
stu2.gender = 'male'

# 打印输出查看指定是否成功
print(dir(stu2))
#  'age', 'gender', 'name', 'school', 'show'] <--前面的一堆就不剪切了，这里查看发现我们指定的gender属性是成功指定了的
# 为了进行参考对比，我们在这里输出stu1的各种属性
print(dir(stu1))
# 'age', 'name', 'school', 'show'] <--可以发现它没有gender属性
stu2.introduce = self_intc #动态绑定一个方法，注意别写括号，不然就是把函数执行后的结果赋予给self.introduce了，如果有疑惑记得回到基础篇的装饰器那里学习那里的一些细节

# 调用我们指定好的实例方法

stu2.introduce() #这样相当于直接运行了self_intc
# 这里的结果就是self_intc函数运行的返回值，即打印输出的那句话