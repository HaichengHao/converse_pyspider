# @Editor    : 百年
# @FileName  :09封装.py
# @Time      :2024/4/19 14:07
# 封装 ：提高程序的安全性
# 1. 将数据（属性）和行为(方法)包装到类对象中，在方法内部对属性进行操作，在
# 类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而降低复杂度
# 2. 在python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象之外被访问，
# 就将其声明为私有(见08属性的设置)
# 学习这一节时不用有其它思考，只需要将其作为属性设置的引申即可

# 先来定义一个类作为对照
'''
class Car():
    def __init__(self,brand_):
        self.brand = brand_
    def start_engine(self): #定义一个实例方法
        print(f'{self.brand}的引擎启动了')

# 定义一个实例对象
mbz = Car(brand_='梅赛德斯奔驰')
# 调用实例方法
mbz.start_engine()
# 梅赛德斯奔驰的引擎启动了
'''

'''
# 这次在定义一个生产编号，作为一个私有的对象，不可以被外部直接访问
class Car():
    def __init__(self,brand_,car_id_):
        self.brand = brand_
        self.__car_id = car_id_
    def start_engine(self): #定义一个实例方法
        print(f'{self.brand}的引擎启动了')

# 定义一个实例对象
mbz = Car(brand_='梅赛德斯奔驰',car_id_='202309120140')
# 调用实例方法
mbz.start_engine()
# 梅赛德斯奔驰的引擎启动了
'''
# 尝试在外部访问car_id
'''
try:
    print(mbz.car_id)
except BaseException as e:
    print(e)
    # 'Car' object has no attribute 'car_id' <--很明显，不可以被外部直接访问
    '''

# 接下来我们按照上节课的第一种访问方式来进行访问
# print(mbz._Car__car_id) #第一种访问方式，即实例对象名._类名__私有属性名
# 202309120140 <--访问成功


# 这里写第二种方式，为了不混淆，先将其它的代码注释掉

class Car():
    def __init__(self,brand_,car_id_):
        self.brand = brand_
        self.__car_id = car_id_
    def start_engine(self): #定义一个实例方法
        print(f'{self.brand}的引擎启动了')
    @property
    def car_id(self):
        return self.__car_id
    # 创建可修改的car_id
    @car_id.setter
    def car_id(self,value):
        self.__car_id = value


# 定义一个实例对象
mbz = Car(brand_='梅赛德斯奔驰',car_id_='202309120140')

# 第二种访问方式即先设置装饰器，利用装饰器将私有属性作为普通属性进行返回

# 尝试像访问普通属性那样直接访问私有属性
print(mbz.car_id)
# 202309120140 <--成功

# 对car_id进行修改
mbz.car_id = '20240419brandnew'
print(mbz.car_id)
# 20240419brandnew <--修改成功，买车一定要注意是不是翻新的