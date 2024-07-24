# @Editor    : 百年
# @FileName  :02_多线程实现含有参数的任务.py
# @Time      :2024/7/23 11:28
import time
from threading import Thread
def musicplay(musicname):
    print(f'开始播放音乐：{musicname}')
    time.sleep(0.5)

def movieplay(moviename):
    print(f'开始播放电影：{moviename}')
    time.sleep(0.2)
def gameplay(gamename,username):
    print(f'开始玩{gamename}，游戏名称为：{username}')
    time.sleep(0.3)

if __name__ == '__main__':
    starttime = time.time()
    t1=Thread(target=musicplay, args=('太阳nock',)) #<--注意，使用位置传参方式进行参数传递的话需要传入的是元组
    t2=Thread(target=movieplay, kwargs={'moviename':'大话西游'}) #<--使用关键字传参的话传入的是字典
    t3=Thread(target=gameplay, args=('LOL', '百年')) #<--使用位置传参方式进行传递
    t4=Thread(target=gameplay, kwargs={'username':'百年','gamename':'CFHD'})

    # 开启多线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # 主线程阻塞，直到所有子线程完成
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(f'总耗时{time.time()-starttime}')
    print('所有任务已完成')

# 开始播放音乐：太阳nock
# 开始播放电影：大话西游
# 开始玩LOL，游戏名称为：百年
# 开始玩CFHD，游戏名称为：百年
# 总耗时0.5081782341003418  <--开启多线程后耗费的时间明显比正常单线执行的程序耗时短，如果单线执行，那么最优情况下会是0.5+0.2+0.3*2=1.3s
# 所有任务已完成