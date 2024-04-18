# editor: 百年
# time: 2024/3/7 10:52
# 两个关键字global和nonlocal

# global 变量名  在局部引入全局变量
# a=10
# def func1():
#     # 此时想在变量内部修改全局变量a,只需利用global
#     global a  #把函数体外部的全局变量a引入到函数体内部
#     a=20
#
# func1() #<--执行func1()即将a的值指定为20
# print(a) #打印输出，结果为20

# nonlocal 变量名  在局部引入外层的局部变量
# 向外找一层，看看有没有该变量，如果有就引入，如果没有，继续向外一层，直到全局(不包括全局)
def func():
    a=10
    def func1():
        nonlocal a
        a=20
    func1()
    print(a)
func()
# 20

# 既然全局变量可以在局部被更改，说明全局变量并不是安全的
# 为了避免这样的危险，需要进行闭包