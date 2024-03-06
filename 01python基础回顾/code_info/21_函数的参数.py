# editor: 百年
# time: 2024/3/6 9:27


# # 函数的定义
# def suzhi(name,level): #形参两个
#     if level==1:
#         print('{0}素质不高'.format(name))
#     elif level == 2:
#         print('{0}素质有待提高'.format(name))
#     elif level == 3:
#         print('{0}素质比较高'.format(name))
#     elif level == 4:
#         print('{0}素质很高'.format(name))
#     elif level >4:
#         print('{0}是大圣人'.format(name))
#
# # 函数调用,传入实参
# suzhi('小明',2)
# suzhi('小红',1)
# suzhi('孔子',99)
# # 小明素质有待提高
# # 小红素质不高
# # 孔子是大圣人

# 案例，数学计算器，实现四则计算
'''def CoMp(a,opt,b):
    if opt=="+":
        print(a+b)
    elif opt=="-":
        print(a-b)
    elif opt=="*":
        print(a*b)
    elif opt=="/":
        print(a/b)
    else:
        print('ERROR')
CoMp(2,'*',5)'''

'''# 实参详细
# 定义一个函数
def eat(main_food,sub_food,soup,sweet):
        print(f'主食:{main_food},辅食:{sub_food},汤品:{soup},甜点:{sweet}')

# 可以进行位置传参，也可进行关键字传参

# 位置传参需要注意顺序
eat('面条','馒头','罗宋汤','大列巴')
# 关键字传参可以不按顺序
eat(main_food='米饭',soup='紫菜蛋花汤',sub_food='荞麦面',sweet='小蛋糕')
# 主食:面条,辅食:馒头,汤品:罗宋汤,甜点:大列巴
# 主食:米饭,辅食:荞麦面,汤品:紫菜蛋花汤,甜点:小蛋糕

# 也可混着写，不过位置参数要写在前面
eat('米饭','面条',soup='小米汤',sweet='法式小面包')
# 主食:米饭,辅食:面条,汤品:小米汤,甜点:法式小面包

# 注意，在Python中的函数，一般都是(args,kwargs) 即位置参数在前，关键字参数在后


'''

'''
# 形参详细
# 位置参数 args
# 关键字参数 kwargs

# 默认值参数演示，如果未指定则按默认值执行，如果指定则按指定的来执行
def personal_info(name,age,gender='男'):
    print(f'姓名:{name},性别:{gender},年龄{age}')

# 函数调用
personal_info('张三',20)
# 姓名:张三,性别:男,年龄:20

personal_info('李四',20,'女')'''
# 姓名:李四,性别:女,年龄20 <--若指定，则按指定的来

# 注意，默认值参数在使用的时候按照规范一定要写到后面
# 错误示例
'''try:
    def ppq(name,gender='女',age):
        print(f'姓名:{name},性别:{gender},年龄{age}')
except BaseException as e:
    print(e)
'''
# SyntaxError: non-default argument follows default argument
# 错误提示：非默认值参数放在了默认值参数后面
#所以，默认值参数应当放在后面



# 3动态传参

'''# 个数可变的位置参数
def food(*food):
    print(food)
food('米饭','面条','胡辣汤','油条','豆浆')
# ('米饭', '面条', '胡辣汤', '油条', '豆浆') <--返回的是一个元组
'''
'''# 个数可变的关键字参数
def eat(**food):
    print(food)
eat(main_food='米饭',sub_food='面条',soup='小米汤',sweet='法式小面包')
# {'main_food': '米饭', 'sub_food': '面条', 'soup': '小米汤', 'sweet': '法式小面包'}
#返回的结果是一个字典'''

# 个数可变的位置参数和个数可变的关键字参数可以混合使用
# 但是一定要注意顺序问题
# 个数可变的位置参数需要放在个数可变的关键字参数之前

def food(*food,**other):
    print(food)
    print(other)

# 调用
food('面条','米饭','饺子',soup='小米汤',sweet='鸡蛋糕')
# ('面条', '米饭', '饺子')
# {'soup': '小米汤', 'sweet': '鸡蛋糕'}

# Python 会按照既定的顺序以及规则(即位置参数返回的是一个元组，关键字参数返回的是一个列表)输出

# 注意，一般将默认值参数放在位置参数之后，如果需要改变默认值则利用关键字传参即可
def func1(a,*c,b=10,**d):
    print(a,b,c,d)
func1(1,12,34,67,d=12,e=2)
# 1 10 (12, 34, 67) {'d': 12, 'e': 2}
func1(1,2,3,4,4,b=12,c=11,d=14)
# 1 12 (2, 3, 4, 4) {'c': 11, 'd': 14}

# 总结位置顺序
#  位置参数>可变位置参数>默认值参数>关键字参数>可变关键字参数


# 对于位置参数的解包只需在要解包的对象前加上*,注意需要是列表或者元组
# 对于关键字参数的解包只需在要解包的对象前加上**,注意需要是字典
def fun_1(a,b,c,d):
    print(a,b,c,d)
num_lst=[1,2,3,4]
try:
    fun_1(num_lst)
except BaseException as e:
    print(e)
#     fun_1() missing 3 required positional arguments: 'b', 'c', and 'd'

# 正确做法，解包赋值
fun_1(*num_lst)
# 1 2 3 4

t1=(7,9,0,1)
fun_1(*t1)
# 7 9 0 1


def fun_2(a,b,c,d):
    print(a,b,c,d)
dic_={'a':100,'b':20,'c':90,'d':11}
try:
    fun_2(dic_)
except BaseException as e:
    print(e)
    # fun_2() missing 3 required positional arguments: 'b', 'c', and 'd'
    # 对于关键字参数传入字典也是需要将字典对象进行解包
fun_2(**dic_)
# 100 20 90 11