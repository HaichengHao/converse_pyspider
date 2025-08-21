# @Author    : 百年
# @FileName  :00声明类型.py
# @DateTime  :2025/8/20 21:48

'''
如果我们自定义的函数中有一些是我们想指定到某个内置的类型
那我们可以通过将类型作为函数参数来实现
'''

def get_full_name(first_name:str,last_name:str): #如果不指定类型,那我们就不能舒服的使用字符串类型的首字母大写操作
    #实现首字母大写
    full_name = first_name.title() + "" + last_name.title()
    return full_name