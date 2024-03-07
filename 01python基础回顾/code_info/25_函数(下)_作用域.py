# editor: 百年
# time: 2024/3/7 9:37
a = 10
print(a)
def demo():
    b=2
    print(b)
try:
    print(b)
except BaseException as e:
    print(e)
    # name 'b' is not defined <--在函数内声明的变量不能够在函数外访问
# 全局变量可以被在函数内访问
def demo2():
    print(a)  #《--函数内可以引用全局变量
demo2()
# 10 <--全局变量可以被访问

# 函数嵌套，在函数内调用其它函数
def demo3():
    demo2()
demo3()
# 10

# 注意，顶格声明的函数都是全局的，如果在函数内声明函数将无法在外部访问
def demo4():
    def demo5():
        print(a)
    demo5()
demo4()
# 10

# 尝试调用在Demo4中声明的函数demo5
try:
    demo5()
except BaseException as e:
    print(e)
    # name 'demo5' is not defined
    # 可见，在函数体内声明的函数无法被外部访问


    # 如果非要访问函数体内声名的变量只需将变量返回
def demo6():
    c=34
    def test():
        print(10)
        return test
    return c


# 尝试在函数demo6外部访问c
print(demo6())


