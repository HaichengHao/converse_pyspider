# @Editor    : 百年
# @FileName  :03_多进程执行带有参数的多任务.py
# @Time      :2024/7/13 9:35
# 可以通过位置参数传递，也可以通过关键字参数进行传递
# 如果是位置参数传参，那么必须是一个元组
# 如果是关键字传参，那么必须是一个字典
# todo:如果遗忘，就打开基础回顾的note第21_函数的参数查看
# 注意和之前函数参数传递
import time
import multiprocessing
def playgame(name,user):
    print(f"{name},{user} is playing...")
    time.sleep(2)
    print(f"{name} has finished playing.")
def musicplay(msc_name):
    print(f"{msc_name} is listening...")
    time.sleep(3)
    print(f"{msc_name} has finished listening.")
def movieplay(moviename):
    print(f"{moviename} is playing...")
    time.sleep(3)
    print(f"{moviename} has finished playing.")
def mixvideo(msc1,msc2,msc3):
    print(f"{msc1},{msc2},{msc3} are playing...")
    time.sleep(2)
    print(f"{msc1},{msc2},{msc3} has finished playing.")
if __name__ == '__main__':
    dic1={'moviename':'Titanic'}
    start_time = time.time()
    p1 = multiprocessing.Process(target=playgame,args=('穿越火线','菜鸡'))
    p2 = multiprocessing.Process(target=musicplay,args=('甜甜的',))
    p3 = multiprocessing.Process(target=movieplay,kwargs={'moviename':'《让子弹飞》'})
    p4 = multiprocessing.Process(target=movieplay,kwargs=dic1)
    p5 = multiprocessing.Process(target=mixvideo,kwargs={'msc1':'hh','msc2':'ww','msc3':'aa'})

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    print(f'总耗时:{time.time()-start_time}')
'''
总耗时:0.04520368576049805
穿越火线,菜鸡 is playing...
甜甜的 is listening...
《让子弹飞》 is playing...
Titanic is playing...
hh,ww,aa are playing...
穿越火线 has finished playing.
hh,ww,aa has finished playing.
《让子弹飞》 has finished playing.甜甜的 has finished listening.

Titanic has finished playing.

Process finished with exit code 0


'''


'''
进程执行带有参数的任务传参有两种方式
1 元组方式传参:元组方式传参一定要和参数的顺序保持一致
2 字典方式传参:字典方式传参字典中的key一定要和参数名保持一致
'''