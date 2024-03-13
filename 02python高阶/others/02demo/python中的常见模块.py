# editor: 百年
# time: 2024/3/12 20:53
'''import time
print(time.time())  #整数位是秒，从1970年1月1日至今的时间的秒数
# 1710248278.6659384
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 2024-03-12 21:00:13
print(time.strftime("%X %w"))
# 17:36:23 3

# 计算一组程序执行的耗时
start_time=time.time()
for i in range(10000000):
    i+=1
print(i)
end_time=time.time()
print("总耗时{0}".format(end_time-start_time))
# 总耗时1.0810387134552002
'''


'''import random


# 1. random.random() 随机生成大于0小于1的小数
print(random.random())
# 2.random.randint(x,y) 随机生成大于等于x且小于等于y之间的整数
print(random.randint(3,4))
# 3.random.randrange(x,y)  随机生成大于等于x且小于y之间的整数
print(random.randrange(3,5))
# 4. random.choice(lst_boj) 随机返回列表对象中的值
lst=[i for i in range(10)]
num=random.choice(lst)
print(num)
# 5.random.sample(lst_boj,2) 随机返回列表元素中任意两个随机组合
r=random.sample(lst,3)
r_2=random.sample(lst,4)
print(r)
# [6, 8]
print(r_2)
# [9, 2, 6, 8]

#  6.random.uniform(x,y) 随机生成大于x小于y的小数
print(random.uniform(1,6))
#  7.random.shuffle(lst_obj) 直接将原来的列表元素打乱次序，不会返回一个新的列表
print(random.shuffle(lst))'''


# os 模块
import os
#     1 os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
#     2 os.chdir('dir_name') 改变当前脚本工作目录；相当于shell下的cd (change directory)
#     3 os.curdir 返回当前目录 (.)
#     4 os.pardir 获取当前目录的父目录名 (..)
#     5 os.makedirs('dirname_1/dirname_2')  生成多级目录
#     6 os.mkdir('dirname') 创建文件夹  相当于shell 下的mkdir
#     7 os.rmdir('dirname') 删除文件夹   相当于shell 下的rmdir
#     8 os.listdir('dirname') 列出指定目录下的所有文件和子目录，包括隐藏文件
#     9 os.remove() 删除一个文件
#     10 os.rename('old_name','new_name') 重命名文件 / 目录
#     11 os.stat('path/filename') 获取文件/目录名
#     12 os.sep 输出操作系统指定的路径分隔符 win下为 \\ linux 下为'/'