# @Editor    : 百年
# @FileName  :main.py.py
# @Time      :2024/7/29 7:45
import requests
import time
from threading import Thread
start_time = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/tom',
    'http://127.0.0.1:5000/jay'
]

def get_request(url):
    page_text = requests.get(url=url).text
    print(len(page_text))

# 创建一个线程列表
ts = []
for url in urls:
    # 循环遍历urls列表，为每个url都设置为线程对象
    # 那么这里你可能会问为什么都是t呢？不会乱么?
    # 请回看列表的元素的属性以及集合的元素的属性
    # 集合中是不会出现{t,t,t}这样的，集合会默认去除掉重复的数据
    # 但是列表可以[t,t,t]，所以这里并没有写错，运行试试就知道了
    t = Thread(target=get_request,args=(url,))
    ts.append(t)
    t.start()
#     循环遍历，让每个线程都加入到主程序结束之前，注意，这里还是按序加入
for t in ts:
    t.join()  # 主线程在所有线程都执行完后才结束

    # get_request(url)
print(time.time()-start_time) #程序运行的总耗时

# 非多线程写法
# 2322
# 956
# 509
# 6.048828601837158 <--非多线程写法耗时几乎为6s


# 多线程写法
# 509
# 2322
# 956
# 2.022538661956787

'''
开启多线程是需要付出一定代价的，如果无限制地开启多进程或多线程，会严重占用系统资源
人话:会卡
而且开启多线程会对目标的webserver产生影响，如果不幸弄崩溃人家的服务器是会吃牢饭的
当然你可以使用线程池来适当的解决这个问题
'''
# todo:查看main2.py