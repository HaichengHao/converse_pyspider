# @Editor    : 百年
# @FileName  :15特殊方法.py
# @Time      :2024/4/20 15:34

# 引例
a = 20
b = 100

print(a + b)
# 120.0 思考执行加法运算的底层逻辑
# 实际上是调用了底层的特殊方法a.__add__(b)
# 验证:
c = a.__add__(b)
print(c)


# 120

# 既然两个整数类型的对象可以执行加法操作，那么可以自定义对象重写__add__()实现加法操作

class Student:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)

stu1 = Student('张三')
stu2 = Student('李四')

# 思考一个问题，可以让这stu1+stu2么？很明显是不可以的
try:
    print(stu1+stu2)
#     或者这样写
#     print(stu1.__add__(stu2))
except BaseException as e:
    print(e)

# unsupported operand type(s) for +: 'Student' and 'Student'
# 输出结果表名这样的操作是不支持的

# 如果非要相加咋办呢？那就重写__add__()方法
# 张三李四 <--重写之后运行发现成功

# 接下来说明len()
lst = [x for x in range(1,10)]
print(len(lst))
# 它底层的操作其实是这样：
print(lst.__len__())

# 9
# 9

# 还是那样的问题，我们可不可以输出stu1的长度?
try:
    print(len(stu1))
except BaseException as e:
    print(e)
#     object of type 'Student' has no len()
# 老生常谈，不能，那就自己重写
# 重写完成了，为了区别化，我们再定义几个实例对象
stu3 = Student('alice')
stu4 = Student('jay')
# 现在来测试
print(len(stu3),len(stu4))
# 5 3 <--成功了
# 那么可不可以对stu1和stu2也试试？
print(len(stu1),len(stu2))
# 2 2 <--可见汉字也是可以的
