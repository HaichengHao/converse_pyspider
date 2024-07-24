# @Editor    : 百年
# @FileName  :04线程间的执行顺序.py
# @Time      :2024/7/23 17:24

# 线程是无序执行的
# 获取当前的线程信息通过current_thread方法获取线程对象
import threading

# 获取线程信息的函数
import time


def getinfo():
    time.sleep(0.5) #如果不写这一行，那么运行起来像是有序运行，但是加上这一行再运行就会发现在时间片内线程的运行是无序的
    current_thread=threading.current_thread()
    print(current_thread)

if __name__ == '__main__':
    for i in range(10):
        subprocess = threading.Thread(target=getinfo)
        subprocess.start()
# <Thread(Thread-1 (getinfo), started 1624)>
# <Thread(Thread-2 (getinfo), started 3276)>
# <Thread(Thread-3 (getinfo), started 5752)>
# <Thread(Thread-4 (getinfo), started 14036)>
# <Thread(Thread-5 (getinfo), started 7040)>
# <Thread(Thread-6 (getinfo), started 5532)>
# <Thread(Thread-7 (getinfo), started 12700)>
# <Thread(Thread-8 (getinfo), started 17508)>
# <Thread(Thread-9 (getinfo), started 13516)>
# <Thread(Thread-10 (getinfo), started 16764)>
#
# Process finished with exit code 0


# <Thread(Thread-10 (getinfo), started 9140)>
# <Thread(Thread-7 (getinfo), started 3036)>
# <Thread(Thread-1 (getinfo), started 13384)>
# <Thread(Thread-2 (getinfo), started 18544)><Thread(Thread-9 (getinfo), started 19284)>
# <Thread(Thread-4 (getinfo), started 4388)>
#
# <Thread(Thread-6 (getinfo), started 7928)>
# <Thread(Thread-3 (getinfo), started 1192)>
# <Thread(Thread-8 (getinfo), started 6000)>
# <Thread(Thread-5 (getinfo), started 21732)>
#
# Process finished with exit code 0