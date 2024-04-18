# editor: 百年
# time: 2024/3/7 14:52
'''def func1():
    a=10
    def inner():
        print(a)
        return a
    return inner

ret=func1()  #其实就是inner函数

ret() #《--相当于inner() 即执行inner函数
# 现在有这样的场景，在python中，有某些被定义的功能被定义完后并非直接执行，而是可能要在程序的最后执行
# 为了保证该功能可以被在任何时候执行，Python会把该功能存放在在内存之内
'''

# 写一个计数器，每次a都加一
def func1():
    a=1
    def inner():
        nonlocal a  #<--这样的话a就会常驻于内存
        a+=1
        print(a)
    return inner

res=func1() #相当于res=inner
r1=res() #执行一次inner并将其结果赋予r1  相当于inner()
r2=res() #执行一次inner并将其结果赋予r2  相当于inner()
# 2
# 3
# 通过上面的操作可以看到如果将变量写入函数体内这样可以让变量的更改变得困难


# 如何不通过inner改变a的值该如何改变？
# 不能，这就是闭包的好处，除了在函数内部能修改，其它情况下都不行
# 如果想用，随时执行内层函数即可
# 使用闭包可以防止内存污染，尤其是在企业协作开发时最为有效
# 闭包的本质:内层函数对外层函数的局部变量的使用，此时内层函数被称为闭包函数