# @Editor    : 百年
# @FileName  :05使用类模板创建n多个对象.py
# @Time      :2024/4/18 15:47
# 利用ctrl + alt + l可以使用代码自动排布，更加美观
# 创建一个学生类，要求录入学生信息并保存在列表当中录入完毕之后退出并打印出学生信息
class Student():
    def __init__(self, name_, age_, score_):  # 初始化实例对象
        self.name = name_  # 这样写是为了方便理解，即我们指定的__init__初始化方法中有三个自定义的参数，其作为形参传入并最后被实例对象所接收
        self.age = age_
        self.score = score_

def get_info(stu):
    stulst = []
 # 创建一个空列表用于接收学生信息
    lstdic={'name':f'{stu.name}','age':f'{stu.age}','score':f'{stu.score}'}
    stulst.append(lstdic)
    show_info(stulst) #最后调用show_info方法来展示学生的信息
    # print(stulst)打印一下看一看列表是不是我们想的那个样子
# 定义一个方法，用于展示学生的信息
def show_info(lst):
    for i in range(len(lst)):
        print(f"姓名:{lst[i].get('name')},年龄:{lst[i].get('age')},分数:{lst[i].get('score')}")

# 创建实例对象
stu1 = Student('张三',12,98)
stu2 = Student('李四',14,99)
stu3 = Student('王五',12,100)
get_info(stu1)
get_info(stu2)
get_info(stu3)

print(type(stu1),type(stu2),type(stu3))

'''
姓名:张三,年龄:12,分数:98
姓名:李四,年龄:14,分数:99
姓名:王五,年龄:12,分数:100
<class '__main__.Student'> <class '__main__.Student'> <class '__main__.Student'>'''
