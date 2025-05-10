 

###### 在之前的[【python】详解threading模块：基本概念、join阻塞和setDaemon守护主线程（一）](https://blog.csdn.net/brucewong0516/article/details/81028716)一文中，是有对[多线程](https://so.csdn.net/so/search?q=%E5%A4%9A%E7%BA%BF%E7%A8%8B&spm=1001.2101.3001.7020)进行一个详细的梳理的。其中就提到了线程锁这一功能。主要基于Rlock实现。本文将进一步总结，丰富线程锁内容。

在使用多线程的应用下，如何保证[线程安全](https://so.csdn.net/so/search?q=%E7%BA%BF%E7%A8%8B%E5%AE%89%E5%85%A8&spm=1001.2101.3001.7020)，以及线程之间的同步，或者访问共享变量等问题是十分棘手的问题，也是使用多线程下面临的问题，如果处理不好，会带来较严重的后果，使用python多线程中提供Lock 、Rlock 、Semaphore 、Event 、Condition 用来保证线程之间的同步，后者保证访问共享变量的互斥问题。

*   Lock & RLock：互斥锁，用来保证多线程访问共享变量的问题
*   Semaphore对象：Lock互斥锁的加强版，可以被多个线程同时拥有，而Lock只能被某一个线程同时拥有。
*   Event对象：它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号后让其执行操作。
*   Condition对象：其可以在某些事件触发或者达到特定的条件后才处理数据

##### 1、Lock(互斥锁)

*   请求锁定 — 进入锁定池等待 — — 获取锁 — 已锁定— — 释放锁

Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。  
可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。  
构造方法：mylock = Threading.Lock( )  
实例方法：

1.  acquire(\[timeout\]): 使线程进入同步阻塞状态，尝试获得锁定。
2.  release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

实例一（未使用锁）：

```
import threading
import time

num = 0

def show(arg):
    global num
    time.sleep(1)
    num +=1
    print('bb :{}'.format(num))

for i in range(5):
    t = threading.Thread(target=show, args=(i,))  # 注意传入参数后一定要有【，】逗号
    t.start()

print('main thread stop')

--------------------------------------------------------------------------
main thread stop
bb :1
bb :2
bb :3bb :4
bb :5
```

实例二（使用锁）

```
import threading
import time

num = 0

lock = threading.RLock()


# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    print(num)
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
------------------------------------------------------------------
1
2
3
4
5
6
7
8
9
10
#可以看出，全局变量在在每次被调用时都要获得锁，才能操作，因此保证了共享数据的安全性
```

**对于Lock对象而言，如果一个线程连续两次release，使得线程死锁**。所以Lock不常用，一般采用Rlock进行[线程锁](https://so.csdn.net/so/search?q=%E7%BA%BF%E7%A8%8B%E9%94%81&spm=1001.2101.3001.7020)的设定。

```
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num 
        time.sleep(1)

        if lock.acquire(1):  
            num = num+1
            msg = self.name+' set num to '+str(num)
            print(msg)
            lock.acquire()
            lock.release()
            lock.release()
num = 0
lock = threading.Lock()
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
------------------------------------------------------
Thread-12 set num to 1
```

##### 2、RLock(可重入锁)

RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。**RLock使用了“拥有的线程”和“递归等级”的概念**，处于锁定状态时，RLock被某个线程拥有。**拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数**。可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。  
构造方法：mylock = Threading.RLock()  
实例方法：acquire(\[timeout\])/release(): 跟Lock差不多。

*   实例解决死锁，调用相同次数的acquire和release，保证成对出现

```
import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire() #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()

print(rLock.acquire())
```

*   详细实例：

```
import threading
mylock = threading.RLock()
num = 0
class WorkThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name
    def run(self):
        global num
        while True:
            mylock.acquire()
            print('\n%s locked, number: %d' % (self.t_name, num))
            if num >= 2:
                mylock.release()
                print('\n%s released, number: %d' % (self.t_name, num))
                break
            num += 1
            print('\n%s released, number: %d' % (self.t_name, num))
            mylock.release()
def test():
    thread1 = WorkThread('A-Worker')
    thread2 = WorkThread('B-Worker')
    thread1.start()
    thread2.start()
if __name__ == '__main__':
    test() 
--------------------------------------------------
A-Worker locked, number: 0

A-Worker released, number: 1

A-Worker locked, number: 1

A-Worker released, number: 2

A-Worker locked, number: 2

A-Worker released, number: 2

B-Worker locked, number: 2

B-Worker released, number: 2
```

本文转自 <https://blog.csdn.net/brucewong0516/article/details/81050939>，如有侵权，请联系删除。